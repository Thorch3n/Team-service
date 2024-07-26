# Engineering Teams Management Service

Этот проект предоставляет REST сервис для управления командами инженеров. Он разработан с использованием Django и Django REST Framework, и может быть развернут в Docker и Kubernetes.

## Оглавление

- [Особенности](#особенности)
- [Требования](#требования)
- [Установка](#установка)
- [Запуск приложения](#запуск-приложения)
- [Запуск тестов](#запуск-тестов)
- [Docker](#docker)
- [Kubernetes](#kubernetes)
- [API](#api)

## Особенности

- Создание команды
- Изменение состава команды
- Удаление команды
- Поддержка деплоя в Kubernetes
- Встроенные health-check'и

## Требования

- Python 3.9
- Django 4.2.2
- Docker
- Docker Compose (опционально для локальной разработки)
- Kubernetes (для деплоя в k8s)

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Thorch3n/Team-service.git
    cd engineering-teams
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск приложения

1. Примените миграции базы данных:

    ```bash
    python manage.py migrate
    ```

2. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

Приложение будет доступно по адресу `http://localhost:8000`.

## Запуск тестов

Запустите тесты с помощью следующей команды:

```bash
python manage.py test
```

## Docker
### Сборка Docker-образа
1. Сборка Docker-образа:
```bash
docker build -t engineering_teams:latest .
```
2. Запуск контейнера:
```bash
docker run -p 8000:8000 engineering_teams:latest
```

## Docker Compose
Для удобного запуска с Docker Compose используйте docker-compose.yml

### Запуск с Docker Compose
```bash
docker-compose up --build
```
## Kubernetes
Для деплоя в Kubernetes существуют следующие манифесты:
- Deployment
- Service

### Примените манифесты:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## API

### Создание команды

```
POST /api/teams/
Content-Type: application/json

{
  "name": "Team Alpha"
}
```
### Изменение состава команды
```
PUT /api/teams/{id}/
Content-Type: application/json

{
  "members": ["Alice", "Bob"]
}
```

### Удаление команды
```bash
DELETE /api/teams/{id}/
```
