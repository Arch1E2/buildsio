#!/bin/sh

echo "Run Back"
sleep 3

python manage.py makemigrations
python manage.py migrate
python manage.py get_valutes
python manage.py get_valute_rates
crontab ../etc/cron.d/get_valute_rates
touch ../var/log/cron.log

python manage.py runserver 0:8000