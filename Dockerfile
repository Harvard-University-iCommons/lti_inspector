FROM python:2
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/logs
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
