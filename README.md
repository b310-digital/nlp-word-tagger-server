# NLP Word Tagger Server
Mini Python Server that receives a sentence and tokenizes &amp; tags included words.

## Install

`pip3 install -r requirements.txt`

## Start

`python3 server.py`

And then simply send the server on the route `/tag_words?lang=en` a body with text.

## Docker

The docker file features the following env variables, e.g.:

```
BASIC_AUTH_ENABLED: true
BASIC_AUTH_USER_NAME: admin
BASIC_AUTH_USER_PASSWORD: test
SERVER_PORT: 8080
SERVER_HOST: 0.0.0.0
```

## Acknowledgements

- HanTa: https://github.com/wartaal/HanTa