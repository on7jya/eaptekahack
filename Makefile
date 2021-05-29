build:
	docker build -t local/eaptekahack_python:latest -f _docker/python_base/Dockerfile . && \
	docker-compose build app
start:
	docker-compose up -d
start-app:
	docker-compose up -d app
stop:
	docker-compose down
restart:
	docker-compose down
	docker build  -t local/eaptekahack_python:latest -f _docker/python_base/Dockerfile . && \
	docker-compose build  app
	docker-compose up -d
format:
	pre-commit run -a