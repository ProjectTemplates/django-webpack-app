# Template for a modern Django app

Use with cookiecutter: **`cookiecutter https://github.com/ProjectTemplates/django-webpack-app.git`**

Generates a foundation for a **Django** app with Django Rest Framework and some utilities, can optionally add **redis** for storage and session cache. Uses **poetry** for dependency resolution.

Includes configured [webpack.config.js](https://github.com/ProjectTemplates/django-webpack-app/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/core/webpack.config.js), that allows to use all modern tools and libs for writing your JS and then embedding it in django templates by building a bundle and serving it as a static file (see `collect` command in Makefile and [django-webpack-loader](https://github.com/jezdez/django-webpack-loader) for details)

*Automatically* adds dockerfiles for everything, as well as **docker-compose.yml** for development and automatic setup of all services (nginx, db, redis, etc.). Also generates a simple nginx config - for routing requests to django and serving static.

Uses **PostgreSQL** for storage, but you can change it to any other SQL database after generation.

> Note: this template is a bit opinionated

---

Шаблон для современного Django приложения.

Генерирует каркас django-сервиса с настроенным nginx, базой, и опциональным redis (для использования как кэш сессий, либо для какой-либо бизнес-логики) и некоторыми дополнительными пакетами (drf, сваггер генератор и пр.). Для контроля зависимостей используется poetry.

Основная фишка - [webpack.config.js](https://github.com/ProjectTemplates/django-webpack-app/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/core/webpack.config.js), на одном уровне с manage.py, позволяющий рядом с разработкой бэкенда писать фронтовый код, с библиотеками, npm и прочим, который затем можно использовать в django-шаблонах - я, например, так рисовал графики в админке. См. [django-webpack-loader](https://github.com/jezdez/django-webpack-loader) (правда тут он настроен чуть иначе чем в примерах)

В качестве хранилища используется PostgreSQL, но после генерации проекта можно заменить на любое другое.

Автоматически генерируется Dockerfile и docker-compose.yml для оркестрации всего этого добра (этот шаблон рассчитан на разработку в докере), включащий nginx с небольшим конфигом, роутящим запросы к джанге и раздающим статику.
