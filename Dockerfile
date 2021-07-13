FROM python:3.8.2

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


RUN SECRET_KEY=$(cd /home/app/web && python3 -c 'import os; os.getenv("SECRET_KEY")' )
RUN cat $SECRET_KEY
RUN bash -c "if [ -z ${SECRET_KEY+x} ]; then SECRET_KEY=fk4fkk034fk040k40k4k04; fi"

RUN python3 /home/app/web/manage.py check

ENTRYPOINT ["/home/app/web/entrypoint.sh"]


