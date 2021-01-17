# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
FROM python:3.7-slim

COPY requirements.txt /app/
WORKDIR /app

RUN pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt

COPY images ./images/
COPY data ./data/
COPY app.py /app/

EXPOSE 8080
CMD python app.py