ARG TAG="3.9.2-alpine3.13"

FROM python:$TAG as dependency
WORKDIR /usr/src/app
COPY ./src/requirements.txt ./
RUN apk add build-base && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base

FROM dependency as app
COPY ./src .
CMD ["python", "main.py"]
