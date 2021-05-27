from django import urls
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user, GenreView, GameView, EventView, ProfileView
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'genres', GenreView, 'genre')
router.register(r'games', GameView, 'game')
router.register(r'events', EventView, 'event')
router.register(r'profile', ProfileView, 'profile')

urlpatterns = [
    path('admin', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('', include('levelupreports.urls')),
]