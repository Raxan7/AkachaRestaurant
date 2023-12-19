#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip

pip install -r requirements.txt

# python3 manage.py dbrestore --noinput

python3 manage.py makemigrations
python3 manage.py migrate

DJANGO_SUPERUSER_EMAIL="atmaiwiz@gmail.com" \
DJANGO_SUPERUSER_FIRST_NAME="Anania" \
DJANGO_SUPERUSER_MIDDLE_NAME="Tenson" \
DJANGO_SUPERUSER_LAST_NAME="Mtawa" \
DJANGO_SUPERUSER_PASSWORD="1234" \
python3 manage.py createsuperuser --noinput

python3 manage.py collectstatic --no-input

#python3 manage.py dbbackup --noinput
