from django.db import models


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

    subcategory = models.ForeignKey('SubCategory', blank=True, on_delete=models.PROTECT, verbose_name='Категория')


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

""" Новости """
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    text = models.TextField(verbose_name='Текст новости')

    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def get_absolute_url(self):
        return reverse('news', kwargs={'slug': self.slug})

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
