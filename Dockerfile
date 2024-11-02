FROM python:3.12

RUN \
    --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update \
 && apt-get install -y openjdk-17-jre

RUN \
    --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip wheel \
 && pip install pyspark==3.5.3

ADD run.py /app/run.py
