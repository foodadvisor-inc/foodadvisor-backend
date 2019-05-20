from django.contrib import admin
from django.urls import re_path, include

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='USERS API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^schema/', schema_view, name="docs"),
    re_path(r'auth/', include('api.urls')),
    re_path(r'api/', include('foodadvisor.urls'))
]
