FROM python:3.7.2-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /ERPv/
COPY . .
RUN pip install pipenv && pipenv install
ENTRYPOINT [ "pipenv", "run" ]
CMD [ "gunicorn", "main.wsgi", "-b", "0.0.0.0:8000", "-w", "3" ]

