FROM python:3.7.2-alpine AS base
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /ERPv/

FROM base AS build
COPY Pipfile* ./
RUN pip install pipenv && pipenv install --system --deploy

FROM build AS final
COPY . .
ENTRYPOINT [ "pipenv", "run" ]
CMD [ "gunicorn", "main.wsgi", "-b", "0.0.0.0:8000", "-w", "3" ]
