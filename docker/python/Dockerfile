FROM python:3.10.2-alpine3.15

RUN apk update &&\
    apk upgrade
RUN apk add --no-cache \
      gcc \
      g++ \
      curl \
      git \
      libpq \
      libpq-dev

# poetryインストール
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH=$PATH:/root/.poetry/bin:/root/.poetry/env
RUN poetry config virtualenvs.in-project true
