from django.urls import re_path, include

urlpatterns = [
    re_path(r'', include('rest_auth.urls')),
    re_path(r'^registration/', include('rest_auth.registration.urls')),
]
