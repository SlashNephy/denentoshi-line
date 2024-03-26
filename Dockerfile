FROM python:alpine@sha256:c7eb5c92b7933fe52f224a91a1ced27b91840ac9c69c58bef40d602156bcdb41

COPY ./requirements.txt /tmp/requirements.txt
RUN apk add --update --no-cache --virtual .build-deps \
        build-base \
        linux-headers \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt \
    && apk del --purge .build-deps

LABEL org.opencontainers.image.source="https://github.com/SlashNephy/denentoshi-line"
WORKDIR /
COPY ./app.py /app.py
ENTRYPOINT ["python", "-u", "/app.py"]
