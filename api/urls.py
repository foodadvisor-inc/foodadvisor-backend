from django.urls import re_path, include

import api.views as views

urlpatterns = [
    re_path(r'', include('rest_auth.urls')),
    re_path(r'^registration/', include('rest_auth.registration.urls')),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^google/', views.GoogleLogin.as_view(), name='google_login'),
    re_path(r'^profile/', include('profile.urls')),
]
