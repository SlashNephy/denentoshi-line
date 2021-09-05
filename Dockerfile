FROM python:alpine

COPY ./requirements.txt /tmp/requirements.txt
RUN apk add --update --no-cache --virtual .build-deps \
        build-base \
        linux-headers \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt \
    && apk del --purge .build-deps

WORKDIR /
COPY ./app.py /app.py
ENTRYPOINT ["python", "-u", "/app.py"]
