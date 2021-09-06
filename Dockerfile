FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /url_shortener
RUN mkdir /logs

WORKDIR /url_shortener

COPY requirements.txt /url_shortener/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /url_shortener/