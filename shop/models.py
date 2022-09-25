from django.db import models

from django.urls import reverse

#-----------------------------------------------------------------------------------------

""" Продукт """
class Product(models.Model):
    title = models.CharField(blank=True, max_length=100, verbose_name='Название')
    mini_description = models.TextField(blank=True, verbose_name='Небольшое описание')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    product_characteristics = models.TextField(blank=True, verbose_name='Характеристики товара')

    sale = models.BooleanField(blank=True, verbose_name='Распрадажа', default=False)
    buyer_choice = models.BooleanField(blank=True, verbose_name='Выбор покупателя', default=False)
    novelties = models.BooleanField(blank=True, verbose_name='Новинки', default=False)

    old_price = models.CharField(max_length=150, blank=True, verbose_name='Старая цена')
    new_price = models.CharField(max_length=150, blank=True, verbose_name='Новая цена')

    subcategory = models.ForeignKey('SubCategory', blank=True, on_delete=models.PROTECT, verbose_name='Подкатегория')

    #def get_absolute_url(self):
    #    return reverse('get_new', kwargs={'slug': self.slug})

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

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

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
