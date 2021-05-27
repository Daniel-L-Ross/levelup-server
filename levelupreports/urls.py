from django.urls import path
from django.urls.conf import include
from .views import usergame_list

urlpatterns = [
    path('reports/usergames', usergame_list),
]
