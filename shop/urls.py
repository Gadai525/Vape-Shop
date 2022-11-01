from django.urls import path

from .views import *

urlpatterns = [

    path('search/', search, name='search'),

    path('', index, name='home_page'),
    path('catalog/', catalog, name='catalog'),

    path('news/', all_news, name='all_news'),
    path('news/<str:slug>/', get_new, name='get_new'),

    path('category/<str:slug_category>/', get_category, name='get_category'),
    path('subcategory/<str:slug_category>/<str:slug_subcategory>/', get_subcategory, name='get_subcategory'),
    path('product/<str:slug_category>/<str:slug_subcategory>/<str:slug_product>/', get_product, name='get_product'),

    path('brends/<str:slug_brend>/', get_brend, name='get_brend'),
    path('bonuses-gifts/', bonuses_gifts, name='bonuses_gifts'),
    path('delivery/', delivery, name='delivery'),
    path('payment/', payment, name='payment'),
    path('how_to_order/', how_to_order, name='how_to_order'),
    path('guarantees/', guarantees, name='guarantees'),
    path('help/', help, name='help'),
    path('all-stock/', stock, name='stock'),
    path('stock/<str:slug_stock>/', get_stock, name='get_stock'),
    path('about-company/', about_company, name='about_company'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('age-limit/', age_limit, name='age_limit'),
]
