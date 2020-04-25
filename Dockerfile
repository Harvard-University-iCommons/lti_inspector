FROM alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/logs
WORKDIR /code
RUN apk update
RUN apk add build-base python2-dev py2-pip gcc libxml2-dev libxslt-dev
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN chmod a+x /code/docker-entrypoint.sh
RUN apk del build-base gcc
ENTRYPOINT ["/code/docker-entrypoint.sh"]
EXPOSE 8000
