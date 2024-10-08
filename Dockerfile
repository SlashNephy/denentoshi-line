FROM python:alpine@sha256:81362dd1ee15848b118895328e56041149e1521310f238ed5b2cdefe674e6dbf

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
