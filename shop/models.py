from django.db import models

from django.urls import reverse

#-----------------------------------------------------------------------------------------

""" Продукт """
class Product(models.Model):
    title = models.CharField(blank=True, max_length=100, verbose_name='Название')
    mini_description = models.TextField(blank=True, verbose_name='Небольшое описание')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    product_characteristics = models.TextField(blank=True, verbose_name='Характеристики товара')
    main_image = models.ImageField(upload_to='media/images-product/%Y/%m/%d/', verbose_name='Изображения')
    sale = models.BooleanField(blank=True, verbose_name='Распрадажа', default=False)
    buyer_choice = models.BooleanField(blank=True, verbose_name='Выбор покупателя', default=False)
    novelties = models.BooleanField(blank=True, verbose_name='Новинки', default=False)

    old_price = models.CharField(max_length=150, blank=True, verbose_name='Старая цена')
    new_price = models.CharField(max_length=150, blank=True, verbose_name='Новая цена')

    subcategory = models.ForeignKey('SubCategory', blank=True, on_delete=models.PROTECT, verbose_name='Подкатегория')
    brend = models.ForeignKey('Brends', on_delete=models.CASCADE, verbose_name='Бренд')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def get_absolute_url(self):
        return reverse('get_product', kwargs={'slug_product': self.slug, 'slug_category': self.subcategory.category.slug, 'slug_subcategory': self.subcategory.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

#-----------------------------------------------------------------------------------------

""" Категория """
class Category(models.Model):
    title = models.CharField(db_index=True, max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='media/images-category/%Y/%m/%d/', verbose_name='Изображения')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def get_absolute_url(self):
        return reverse('get_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

#-----------------------------------------------------------------------------------------
""" Бренды """
class Brends(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование бренда')
    image = models.ImageField(upload_to='media/images-brends/%Y/%m/%d/', verbose_name='Изображения')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)


    def get_absolute_url(self):
        return reverse('get_brend', kwargs={'slug_brend': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Бренды'
        verbose_name = 'Бренд'

#-----------------------------------------------------------------------------------------

""" Новости """
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст новости')
    image = models.ImageField(upload_to='media/images-news/%Y/%m/%d/', verbose_name='Изображение')

    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def get_absolute_url(self):
        return reverse('get_new', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-created_at']

#-----------------------------------------------------------------------------------------

""" Подкатегория """
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Подкатегория')
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def get_absolute_url(self):
        return reverse('get_subcategory', kwargs={'slug_subcategory': self.slug, 'slug_category': self.category.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Подкатегории'
        verbose_name = 'Подкатегория'

#-----------------------------------------------------------------------------------------

""" Галерея """
class Gallary(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='author_article_set')
    image = models.ImageField(upload_to='media/images-products/%Y/%m/%d/', verbose_name='Изображения')

    class Meta:
        verbose_name_plural = 'Изображения к продуктам'
        verbose_name = 'Изображение к продукту'

#-----------------------------------------------------------------------------------------

""" Цвет """
class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='author_article_sett')
    color = models.CharField(blank=True, max_length=150, verbose_name='Описание цвета')
    color_image = models.ImageField(upload_to='media/color-image/%Y/%m/%d/', verbose_name='Изображения')

    class Meta:
        verbose_name_plural = 'Цвета продуктов'
        verbose_name = 'Цвет продукта'

""" Никобустер """
class Nicobooster(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField(max_length=150, verbose_name='Крепость')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Никобустеры'
        verbose_name = 'Никобустер'

#-----------------------------------------------------------------------------------------

""" Крепость """
class Fortress(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField(max_length=150, verbose_name='Крепость')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Крепости'
        verbose_name = 'Крепость'

#-----------------------------------------------------------------------------------------

""" Вкус """
class Tastes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField(max_length=200, verbose_name='Название вкуса')
    image = models.ImageField(upload_to='media/tastes-image/%Y/%m/%d/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Вкусы'
        verbose_name = 'Вкус'

#-----------------------------------------------------------------------------------------

""" Объем """
class Volume(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    title = models.CharField(max_length=150, verbose_name='Объем')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Объемы'
        verbose_name = 'Объем'

#-----------------------------------------------------------------------------------------
















class Bonuses_gifts(models.Model):
    text = models.TextField(verbose_name='Бонусы и подарки')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural='Бонус и подарок'
        verbose_name = 'Бонусы и подарки'

class Delivery(models.Model):
    text = models.TextField(verbose_name='Доставка')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural='Доставка'
        verbose_name = 'Доставки'

class Payment(models.Model):
    text = models.TextField(verbose_name='Оплата')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural='Оплата'
        verbose_name = 'Оплата'

class How_to_order(models.Model):
    text = models.TextField(verbose_name='Как заказать')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural='Как заказать'
        verbose_name = 'Как заказать'

class Guarantees(models.Model):
    text = models.TextField(verbose_name='Гарантии')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural='Гарантия'
        verbose_name = 'Гарантии'

#class Contact(models.Model):
#    text = models.TextField(verbose_name='Контакты')

#    time = models.CharField(max_length=250, verbose_name='Режим работы')
#    phone = models.CharField(max_length=100, verbose_name='Номер')

#    def __str__(self):
#        return self.text

#    class Meta:
#        verbose_name_plural='Контакт'
#        verbose_name = 'Контакты'

class MainPage(models.Model):
    text = models.TextField(verbose_name='Описание на главное странице')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural='Описание на главное странице'
        verbose_name = 'Описание на главное странице'

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
