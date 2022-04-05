FROM python:3.10-alpine
ENV LANG "en_US.UTF-8"
ENV LANGUAGE "en_US:en"
ENV LC_ALL "en_US.UTF-8"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && apk upgrade

WORKDIR /app
COPY main.py .
COPY requirements.txt .
COPY server server
RUN \
    apk add gcc musl-dev python3-dev libffi-dev openssl-dev && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

USER nobody:nobody
EXPOSE 3200
ENTRYPOINT  ["python", "main.py"]