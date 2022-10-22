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

    mainpage = MainPage.objects.all()

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
        'mainpage': mainpage,
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

#-----------------------------------------------------------------------------------------

def get_category(requests, slug_category):
    product = Product.objects.filter(subcategory__category__slug=slug_category)
    category = Category.objects.all()
    #image = Gallary.objects.filter(product__subcategory__category__slug=slug)[0]


    context = {
        'title': 'str(Category.objects.get(slug=slug_category))',
        'product': product,
        'category': category,
        #'image': image,
    }
    return render(requests, template_name='shop/get_category.html', context=context)

#-----------------------------------------------------------------------------------------

def get_subcategory(requests, slug_category, slug_subcategory):

    context = {
        'title': '1sdfsdf',
    }
    return render(requests, template_name='shop/get_subcategory.html', context=context)

#-----------------------------------------------------------------------------------------

def get_product(requests, slug_product, slug_category, slug_subcategory):
    get = Product.objects.filter(slug=slug_product)
    context = {
        'title': 'asdasdas',
        'get': get,
    }
    return render(requests, template_name='shop/get_product.html', context=context)


def get_brend(requests, slug_brend):
    category_brend = Brends.objects.all()
    #brend = Product.objects.filter(brend__slug=slug_brend)
    context = {
        'category_brend': category_brend,
    #    'brend': brend,
        'title': 'titleee',
    }
    return render(requests, template_name='shop/get_brend.html', context=context)


def bonuses_gifts(requests):
    bonuses_gifts = Bonuses_gifts.objects.first()

    context = {
        'bonuses_gifts': bonuses_gifts,
        'title': 'Бонусы и подарки',
    }
    return render(requests, template_name='shop/bonuses_gifts.html', context=context)

def delivery(requests):
    delivery = Delivery.objects.first()

    context = {
        'title': 'asdasd',
        'delivery': delivery,
    }

    return render(requests, template_name='shop/delivery.html', context=context)

def payment(requests):
    payment = Payment.objects.first()

    context = {
        'title': 'asdasd',
        'payment': payment,
    }

    return render(requests, template_name='shop/payment.html', context=context)

def how_to_order(requests):
    how_to_order = How_to_order.objects.first()

    context = {
        'title': 'fsdfsd',
        'how_to_order': how_to_order,
    }

    return render(requests, template_name='shop/how_to_order.html', context=context)

def guarantees(requests):
    guarantees = Guarantees.objects.first()

    context = {
        'title': 'asdas',
        'guarantees': guarantees,
    }

    return render(requests, template_name='shop/guarantees.html', context=context)

def help(requests):
    help = Help.objects.all()

    context = {
        'title': 'aasdad',
        'help': help,
    }

    return render(requests, template_name='shop/help.html', context=context)
