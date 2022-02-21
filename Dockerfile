FROM python:3-slim AS development_build

WORKDIR /app

# Requires ENV argument (used in production), by default dev
ARG ENV=dev

# python:
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
# pip:
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100
# poetry:
ENV POETRY_VERSION=1.0.5
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'


RUN pip install "poetry==$POETRY_VERSION" && poetry --version
RUN if [ "$ENV" = "dev" ]; then apt-get update -y && apt-get install -y git; fi

COPY pyproject.toml poetry.lock /app/
RUN if [ "$ENV" != "dev" ]; then poetry install --no-dev; else poetry install; fi
RUN apt-get update -y && apt-get install -y build-essential

COPY . .