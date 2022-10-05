from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home_page'),
    path('catalog/', catalog, name='catalog'),
    path('news/', all_news, name='all_news'),
    path('news/<str:slug>/', get_new, name='get_new'),
    path('<slug:slug>/', get_category, name='get_category'),
    path('<str:slug_category>/<str:slug_subcategory>/', get_subcategory, name='get_subcategory'),
    path('<str:slug_category>/<str:slug_subcategory>/<str:slug_product>/', get_product, name='get_product'),
]
