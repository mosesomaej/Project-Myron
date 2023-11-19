# FROM python:3-alpine
# ENV PYTHONUNBUFFERED=1
# WORKDIR /app
# COPY requirements.txt requirements.txt
# RUN pip3 install --upgrade pip
# RUN pip3 install -r requirements.txt
# COPY . /app
# EXPOSE 8000

# Stage 1: Build Stage
FROM python:3-alpine AS builder

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Stage 2: Production Stage
FROM python:3-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY --from=builder /app /app

COPY . /app

EXPOSE 8000
