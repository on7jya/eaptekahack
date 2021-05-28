FROM python:3.8-slim-buster

WORKDIR /eaptekahack
RUN pip install -U pip && pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements --dev > requirements.txt && pip install -r /tmp/requirements.txt
