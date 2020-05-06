from python:3.8.2-alpine3.11

WORKDIR /root/web
COPY . /root/web


RUN apk add --update \
        build-base \
        linux-headers

RUN pip3 install --upgrade pip \
  && pip3 install virtualenv \ 
  && pip3 install flask \
  && pip3 install grpcio \
  && pip install google \
  && pip install protobuf 

EXPOSE 5000

ENTRYPOINT ["python3", "FlaskMain.py"]