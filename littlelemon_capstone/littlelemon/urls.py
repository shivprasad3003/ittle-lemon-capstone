from django.contrib import admin
from django.urls import path, include
from restaurant.views import home
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("api/", include("restaurant.urls")),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
    path("api-auth/", include("rest_framework.urls")),
]
