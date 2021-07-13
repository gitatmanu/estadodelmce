FROM python:3.8.2

ARG SECRET_KEY
RUN echo ${SECRET_KEY}
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

RUN apt-get update \
    && apt-get install -y netcat



# Create an app user in the app group. 
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash app

ENV APP_HOME=/home/app/web

# Create the staticfiles directory. This avoids permission errors. 
RUN mkdir -p $APP_HOME/staticfiles

# Change the workdir.
WORKDIR $APP_HOME



COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . $APP_HOME
RUN chown -R app:app $APP_HOME

USER app:app

ENV SECRET_KEY=${SECRET_KEY}

RUN python3 /home/app/web/manage.py check  --deploy

ENTRYPOINT ["/home/app/web/entrypoint.sh"]


