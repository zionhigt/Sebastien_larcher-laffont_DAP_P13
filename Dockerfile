FROM python/alpine:3.16
RUN apk add python3
RUN python3 manage.py migrate
RUN python3 manage.py runserver
