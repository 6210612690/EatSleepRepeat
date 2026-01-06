ARG PYTHON_VERSION=3.10-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

# Example Dockerfile snippet for a Rails app on Fly.io
RUN apt-get update -qq && \
    apt-get install --no-install-recommends -y build-essential libpq-dev

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY "Agj72rju8cwRpUlhZBwve3SZgUktOWYK9B3KSk0WdFmxIVL3ab"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn","--bind",":8000","--workers","2","EatSleepRepeat.wsgi"]
