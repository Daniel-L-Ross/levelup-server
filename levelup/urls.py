from django import urls
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user, Genres
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'genres', Genres, 'genre')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))
]