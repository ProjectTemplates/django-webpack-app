from django.apps import AppConfig


class ServerConfig(AppConfig):
    name = 'server'
    verbose_name = '{{ cookiecutter.project_name|capitalize }} App'
