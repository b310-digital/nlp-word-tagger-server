FROM python:3.11.1-slim-bullseye as base

WORKDIR /app

COPY requirements.txt /app
COPY server.py /app
RUN pip3 install -r requirements.txt

FROM base as development
FROM base as production
CMD ["python3", "/app/server.py"]