from django.urls import re_path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
schema_view = get_schema_view(title='USERS API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [

    re_path(r'^models/', include(router.urls), name="models"),
    re_path(r'^user/', include('profile.urls')),
]
