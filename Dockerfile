FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY db.sql /code/db.sql

RUN pip install --no-cache-dir Django

EXPOSE 8000
