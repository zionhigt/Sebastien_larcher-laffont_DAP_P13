FROM python/alpine:3.16

RUN python3 manage.py migrate
RUN python3 manage.py runserver
