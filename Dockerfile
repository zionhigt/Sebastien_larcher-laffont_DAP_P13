FROM python:3.9.13-alpine
COPY . /
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
# RUN python3 manage.py runserver