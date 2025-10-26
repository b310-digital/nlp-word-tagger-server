FROM python:3.14.0-slim-trixie AS base

WORKDIR /app

COPY requirements.txt /app
COPY server.py /app
RUN pip3 install --no-cache  -r requirements.txt

FROM base AS development
FROM base AS production
ENV NLTK_DATA=/app-nltk

USER nobody
# create working directory that nobody can download to:
WORKDIR /app-nltk

CMD ["python3", "/app/server.py"]