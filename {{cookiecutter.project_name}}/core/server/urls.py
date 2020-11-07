from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from conf import DEBUG

if DEBUG:
    permission_classes = (permissions.AllowAny,)
else:
    permission_classes = (permissions.IsAdminUser,)

openapi_info = openapi.Info(
    title='{{ cookiecutter.project_name|capitalize }} API',
    default_version='v1',
    description='Server API for data store',
)
schema_view = get_schema_view(
    openapi_info,
    public=True,
    permission_classes=permission_classes,
)

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(
        r'^api/swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    re_path(
        r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
]
