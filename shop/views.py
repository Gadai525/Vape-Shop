from django.shortcuts import render


from shop.models import *


def index(requests):
    all_category = Category.objects.all()

    one_category = Category.objects.all()[0:1]
    two_category = Category.objects.all()[1:2]
    three_categroy = Category.objects.all()[2:3]
    four_category = Category.objects.all()[3:4]

    other_category = Category.objects.all()[4::]

    context = {
        'all_category': all_category,
        'one_category': one_category,
        'two_category': two_category,
        'three_categroy': three_categroy,
        'four_category': four_category,
        'other_category': other_category,
        'title': 'Смокинг-вейпшоп',
    }
    return render(requests, template_name='shop/index.html', context=context)

def catalog(requests):
    all_catalog = Category.objects.all()

    context = {
        'all_catalog': all_catalog,
        'title': 'Каталог'
    }

    return render(requests, template_name='shop/all_catalog.html', context=context)
