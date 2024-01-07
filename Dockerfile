FROM python:3.12.1-slim-bullseye as base

WORKDIR /app

COPY requirements.txt /app
COPY server.py /app
RUN pip3 install --no-cache  -r requirements.txt

FROM base as development
FROM base as production

USER nobody
CMD ["python3", "/app/server.py"]