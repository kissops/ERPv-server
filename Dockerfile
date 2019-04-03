FROM python:3.7.2-alpine AS base
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /ERPv/

FROM base AS build
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM build AS final
COPY . .
CMD [ "gunicorn", "main.wsgi", "-b", "0.0.0.0:8000", "-w", "3" ]
