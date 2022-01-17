FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc default-libmysqlclient-dev

RUN pip install --upgrade pip

RUN pip install poetry && poetry config virtualenvs.in-project true
## CREATE APP USER ##

# Create the home directory for the new app user.
RUN mkdir -p /home/app

# Create an app user so our program doesn't run as root.
RUN groupadd -r app &&\
    useradd -r -g app -d /home/app -c "Docker image user" app

# Set the home directory to our app user's home.
ENV HOME=/home/app
ENV APP_HOME=/home/app/backend

## SETTING UP THE APP ##
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# ***
# Do any custom logic needed prior to adding your code here
# ***

# Copy in the application code.
ADD . $APP_HOME

# Chown all the files to the app user.
COPY --chown=app:app . $APP_HOME

# Change to the app user.
USER app

RUN poetry install

