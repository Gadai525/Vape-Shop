from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home_page'),
    path('catalog/', catalog, name='catalog'),
]
