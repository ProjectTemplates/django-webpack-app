import os


def to_bool(value):
    return (
        value is True or
        (isinstance(value, str) and value.lower() in ['true', 'yes']) or
        (isinstance(value, (int, float)) and value > 0)
    )


bind = '0.0.0.0:{}'.format(os.getenv('GUNICORN_PORT', '8000'))
max_requests = int(os.getenv('GUNICORN_MAX_REQUESTS', '10000'))
max_requests_jitter = int(os.getenv('GUNICORN_MAX_REQUESTS_JITTER', '100'))
user = os.getenv('GUNICORN_USER', 'root')
keepalive = int(os.getenv('GUNICORN_KEEPALIVE', '70'))

reuse_port = to_bool(os.getenv('GUNICORN_REUSE_PORT', True))

accesslog = '-'
errorlog = '-'
print_config = True

workers = int(os.getenv('GUNICORN_WORKERS', '5'))
threads = int(os.getenv('GUNICORN_THREADS', '5'))
