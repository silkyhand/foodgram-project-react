![yamdb_workflow](https://github.com/silkyhand/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)
# Проект Foodgram

Foodgram - сайт для публикации рецептов. Авторизованные пользователи
могут подписываться на понравившихся авторов, добавлять рецепты в избранное,
в покупки, скачать список покупок ингредиентов для добавленных в покупки
рецептов 

# Стек Технологий
Python, Django, Django REST Framework, PostgreSQL, Docker, NGNIX, gunicorn, GitHubActions, Yandex.Cloud.

## Подготовка проекта
### Склонируйте репозиторий на локальную машину: 
```
git clone https://github.com/silkyhand/foodgram-project-react
```
### Подготовить удаленный сервер (например ubuntu на Yandex.Cloud):

- Подключитесь к удаленному серверу(например по протоколу SSH)
- Установите  docker
- Установите docker-compose
- Скопируйте на сервер в home/<ваш_username>/nginx/nginx.conf  
  файл /infra/nginx.conf с локальной машины, предварительно указав в 
  нем IP адрес вашего сервера в строе server_name 
- Скопируйте на сервер в  home/<ваш_username>/docker-compose.yaml 
   файл docker-compose.yml с локальной машины 
- Создайте на сервере файл .env и запишите в него переменные:
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    SECRET_KEY=<секретный ключ проекта django>
    
### Создайте переменные окружения Secrets GitHub  в свой репозиторий с проектом на GitHub:
```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    
    DOCKER_PASSWORD=<пароль от DockerHub>
    DOCKER_USERNAME=<имя пользователя>
    
    SECRET_KEY=<секретный ключ проекта django>

    USER=<username для подключения к серверу>
    HOST=<IP сервера>
    PASSPHRASE=<пароль для сервера, если он установлен>
    SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

    TELEGRAM_TO=<ID чата, в который придет сообщение>
    TELEGRAM_TOKEN=<токен вашего бота>
 ```
 ## Запуск проекта
 
   - Выполните push проекта с локальной машины в GitHub.
   - После прохождения тестов flake8, cборки и отправки образа бекенда на DockerHub,
     деплоя проекта на серевер по указанному адресу в  телеграм придет сообщение "workflow успешно выполнен"
   - На сервере выполните следующие команды:
   
```
    sudo docker-compose exec backend python manage.py migrate 
       
    sudo docker-compose exec backend python manage.py createsuperuse
    
    sudo docker-compose exec backend python manage.py collectstatic --noinput
       
    sudo docker-compose exec backend python manage.py load_ingredients <загрузка файла с ингредиентами>
 ```
    
   - Проект будет доступен по вашему IP адресу


# В настоящий момент проект доступен по адресу
http://51.250.51.196/
