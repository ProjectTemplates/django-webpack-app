import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('server')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.conf')

application = get_wsgi_application()
