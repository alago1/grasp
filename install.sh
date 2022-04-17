#!/usr/bin/env bash

python3.9 -m pip install pipenv
python3.9 -m pipenv install --dev
python3.9 -m pipenv install --system --dev
python3.9 -m pip install pre-commit

pre-commit install
python3.9 -m pipenv run spacy download en_core_web_sm
touch .env
echo 'GOOGLE_APPLICATION_CREDENTIALS="cloud_credentials.json"' > .env
touch cloud_credentials.json