FROM python:3.9 AS base

WORKDIR /app
COPY . .
ARG DATABASE_URL
ARG SECRET_KEY
ENV DATABASE_URL=$DATABASE_URL
ENV SECRET_KEY=$SECRET_KEY

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
