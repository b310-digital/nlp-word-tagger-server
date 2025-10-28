# NLP Word Tagger Server
Mini Python Server that receives a sentence and tokenizes &amp; tags included words.

Supported languages: German and English.

## Configuration

The following settings can be adjusted by environment variables:

- BASIC_AUTH_ENABLED: defaults to true
- BASIC_AUTH_USER_NAME: defaults to admin
- BASIC_AUTH_USER_PASSWORD: defaults to admin
- SERVER_PORT: defaults to 8080
- SERVER_HOST: defaults to 0.0.0.0

## Docker Setup

```
docker build . -t nlp-word-tagger-server
docker run --env BASIC_AUTH_ENABLED=true --env BASIC_AUTH_USER_NAME=admin --env BASIC_AUTH_USER_PASSWORD=test --env SERVER_PORT=8080 --env SERVER_HOST=0.0.0.0 -p 8080:8080 nlp-word-tagger-server 
```

### Docker Compose

```
version: "3.8"

services:
  nlp-word-tagger-server:
    build:
      context: https://github.com/b310-digital/nlp-word-tagger-server.git#main
      target: production
    restart: on-failure
    tty: true
    stdin_open: true
    ports:
      - 8080:8080
    environment:
      BASIC_AUTH_ENABLED: true
      BASIC_AUTH_USER_NAME: admin
      BASIC_AUTH_USER_PASSWORD: test
      SERVER_PORT: 8080
      SERVER_HOST: 0.0.0.0
```

## Manual Setup

### Install

`pip3 install -r requirements.txt`

### Start

`python3 server.py`

## Usage

Simply POST to the server on path `/tagged_words?lang=en` where lang = {en | de} a body with text. Don't forget to provide BASIC AUTH information according to your setup.

Example response for a german query:

```json
[
	{
		"original": "hat",
		"normalized": "haben",
		"wordClass": "VA(FIN)"
	},
	{
		"original": "viele",
		"normalized": "viel",
		"wordClass": "PIAT"
	},
	{
		"original": "Ursprünge",
		"normalized": "Ursprung",
		"wordClass": "NN"
	}
]
```

## Acknowledgements

- HanTa: https://github.com/wartaal/HanTa
- NLTK: https://github.com/nltk/nltk
