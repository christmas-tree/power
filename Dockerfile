FROM gliderlabs/alpine:latest

ADD . /power

VOLUME /power/config

RUN apk add --update --no-cache python py-pip \
    && cd /power \
    && pip install -r requirements.txt

ENTRYPOINT /power/start.sh
