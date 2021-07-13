#!/bin/sh

python manage.py check --deploy


# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations main --noinput 
python manage.py migrate --noinput 

python manage.py collectstatic --noinput

exec "$@"
