FROM python:3.9.2
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean -y && \
    apt-get install -y cron && \
    apt-get install -y --no-install-recommends apt-utils tar git build-essential python3 python3-pip python3-setuptools python3-dev net-tools
# RUN pip install --upgrade pip
# RUN pip install uwsgi 

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY . /backend

WORKDIR /backend
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt
EXPOSE 5000
