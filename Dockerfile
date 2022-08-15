FROM alpine:3.16
RUN apk add python3 py3-pip
COPY . /
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
# RUN python3 manage.py runserver