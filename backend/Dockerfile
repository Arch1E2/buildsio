FROM python:3.8.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./backend .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get -y install cron \
    && apt-get -y install python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 \
    && pip install -U pip \
    && pip install --no-cache-dir -r requirements.txt

RUN chmod +x run.sh

COPY ./backend/get_valute_rates.cron /etc/cron.d/get_valute_rates
RUN chmod 0644 /etc/cron.d/get_valute_rates

ENTRYPOINT [ "/app/run.sh" ]