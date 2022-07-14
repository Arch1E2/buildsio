FROM python:3.8.10

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# RUN apt-get update && apt-get -y install cron vim

WORKDIR /app

COPY ./backend .

RUN pip install -U pip \
    pip install -r requirements.txt

RUN chmod +x run.sh

COPY ./backend/get_valute_rates.cron /etc/cron.d/get_valute_rates
RUN chmod 0644 /etc/cron.d/get_valute_rates
ENTRYPOINT [ "/app/run.sh" ]