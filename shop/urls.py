from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home_page'),
    path('catalog/', catalog, name='catalog'),
    path('news/', all_news, name='all_news'),
    path('news/<str:slug>/', get_new, name='get_new'),
    path('asd/<str:slug>/', get_product_category, name='get_product_category'),
]
