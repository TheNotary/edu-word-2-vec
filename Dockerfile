FROM python:3.11.3-bullseye

WORKDIR /app

COPY main.py .
COPY requirements.txt

