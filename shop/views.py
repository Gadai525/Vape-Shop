from django.shortcuts import render


from shop.models import *


#-----------------------------------------------------------------------------------------

def index(requests):
    all_category = Category.objects.all()
    all_news = News.objects.all()[0:4]
    all_brends = Brends.objects.all()[0:6]

    one_category = Category.objects.all()[0:1]
    two_category = Category.objects.all()[1:2]
    three_categroy = Category.objects.all()[2:3]
    four_category = Category.objects.all()[3:4]

    other_category = Category.objects.all()[4::]

    sale_product = Product.objects.filter(sale=True)[0:4]
    buyer_choice_product = Product.objects.filter(buyer_choice=True)[0:4]
    novelties_product = Product.objects.filter(novelties=True)[0:4]

    context = {
        'all_category': all_category,
        'all_news': all_news,
        'all_brends': all_brends,
        'one_category': one_category,
        'two_category': two_category,
        'three_categroy': three_categroy,
        'four_category': four_category,
        'other_category': other_category,
        'sale_product': sale_product,
        'buyer_choice_product': buyer_choice_product,
        'novelties_product': novelties_product,
        'title': 'Смокинг-вейпшоп',
    }
    return render(requests, template_name='shop/index.html', context=context)

#-----------------------------------------------------------------------------------------

def catalog(requests):
    all_catalog = Category.objects.all()
    context = {
        'all_catalog': all_catalog,
        'title': 'Каталог'
    }
    return render(requests, template_name='shop/all_catalog.html', context=context)

#-----------------------------------------------------------------------------------------

def all_news(requests):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Все новости'
    }
    return render(requests, template_name='shop/all_news.html', context=context)

#-----------------------------------------------------------------------------------------

def get_new(requests, slug):
    new = News.objects.get(slug=slug)
    context = {
        'new': new,
        'title': News.objects.get(slug=slug),
    }
    return render(requests, template_name='shop/get_new.html', context=context)
