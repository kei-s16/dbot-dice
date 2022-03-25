FROM python:3.9.2-alpine3.13

WORKDIR /usr/src/app

COPY ./src/requirements.txt ./

RUN apk add build-base && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base

COPY ./src .

CMD ["python", "main.py"]
