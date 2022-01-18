FROM python:3.10-slim-bullseye


WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc default-libmysqlclient-dev

RUN pip install --upgrade pip

RUN pip install poetry && poetry config virtualenvs.in-project true

# Chown all the files to the app user.
COPY . .

RUN poetry install

