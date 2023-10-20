FROM python:3.11.6-alpine
LABEL maintainer='Grzegorz Zygan'

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG DEV=false

COPY ./api/requirements.txt /tmp/requirements.txt
COPY ./api/requirements.dev.txt /tmp/requirements.dev.txt

COPY ./compose/local/api/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./compose/local/api/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    api-user


USER api-user
WORKDIR /api
