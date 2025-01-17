FROM python:3.9.13-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt && \
python3 manage.py collectstatic
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]