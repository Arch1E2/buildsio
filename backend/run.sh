#!/bin/bash

echo "Run Back"
sleep 3

python manage.py makemigrations
python manage.py migrate
python manage.py get_valutes
python manage.py get_valute_rates
ls
crontab ../etc/cron.d/get_valute_rates
touch ../var/log/cron.log
cron && tail -f ../var/log/cron.log
echo "cron run"
python manage.py runserver 8000

