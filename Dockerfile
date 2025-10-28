FROM python:3.13.9-alpine AS base

WORKDIR /app

COPY requirements.txt /app
COPY server.py /app
RUN pip3 install --no-cache-dir -r requirements.txt

ENV SPACY_MODEL_DIR=/app-spacy-data

RUN python -m spacy download en_core_web_sm
RUN python -m spacy download de_core_news_sm

FROM base AS development
FROM base AS production

USER nobody

CMD ["python3", "/app/server.py"]