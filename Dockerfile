FROM apline:latest

ADD . /power

VOLUME /power/config

RUN apk add --update \
    python \
    py-pip \
    && cd /power \
    && py-pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

RUN /power/start.sh