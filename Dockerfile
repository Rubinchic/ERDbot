FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app

RUN chmod -R 755 /app