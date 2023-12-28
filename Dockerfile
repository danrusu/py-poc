FROM python:3.11-bullseye

WORKDIR /app

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install & use pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

COPY . .

# Creates a non-root user and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ENTRYPOINT [ "python", "-m", "pytest", "-m", "not slow" ]

