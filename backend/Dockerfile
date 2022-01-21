FROM python:3.10-slim-bullseye


WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc default-libmysqlclient-dev

RUN pip install --upgrade pip

RUN pip install poetry && poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /backend/
RUN poetry install -E mysql --no-root
# Chown all the files to the app user.
COPY . /backend

RUN poetry config virtualenvs.create
RUN poetry install -E mysql

