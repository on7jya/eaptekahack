# Бекенд для eaptekahack

Органайзер приема лекарств как часть приложения Сбер Еаптека, который предоставляет возможность пользователю контролировать прием лекарств/товаров (напоминания, информация об остатке)


![](https://img.shields.io/badge/python-black)
![](https://img.shields.io/badge/django-black)
![](https://img.shields.io/badge/postgres-black)
![](https://img.shields.io/badge/drf-black)
![](https://img.shields.io/badge/minio-black)
![](https://img.shields.io/badge/celery-black)
![](https://img.shields.io/badge/redis-black)

[![](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![](https://img.shields.io/badge/code_style-isort-black)
![](https://img.shields.io/badge/code_style-flake8-black)

# Аналитика

[![](https://img.shields.io/badge/Miro-UserStory_Map-00000.svg)](https://miro.com/app/board/o9J_lBnpZfM=/)
[![](https://img.shields.io/badge/Miro-MVP_CJM-00000.svg)](https://miro.com/app/board/o9J_lCcnyWY=/)


# 🚀 Запуск сервиса
1. Установить **python3.8** и менеджер пакетов **pipenv**.
2. Создать .env  `cp .example.env .env`
2. Инициализировать виртуальное окружение и установить зависимости
- `pipenv shell`
- `pipenv install -d`

4. Собрать docker-образы и запустить все
- `make build`
- `make start`
  
  or `make restart` для быстрого рестарта всех контейнеров

5. PostgreSQL в докере
- создать роль и БД
```  
sudo -u postgres psql

create user $DB_USER with password $DB_PASS;
alter role $DB_USER set client_encoding to 'utf8';
alter role $DB_USER set default_transaction_isolation to 'read committed';
alter role $DB_USER set timezone to 'UTC';
create database $DB_NAME owner $DB_USER;

\q
```
- `python manage.py makemigrations` для создания миграции
- `python manage.py migrate` для накатки миграций
- `python manage.py createsuperuser` для создания суперюзера

6. Для загрузки первоначальных данных `python manage.py upload_data`, для обогащения препаратов ссылками  `python manage.py update_img_url`

## Links for localhost
[Admin page](http://localhost:8000/admin)

[Swagger](http://localhost:8000/swagger)

[ReDoc](http://localhost:8000/redoc)

[Flower](http://localhost:5555/)

### Форматирование кода
- `make format`