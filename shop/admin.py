from django.contrib import admin
from django.utils.safestring import mark_safe


from shop.models import *



#-----------------------------------------------------------------------------------------

""" Продукт """
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'mini_description', 'description', 'product_characteristics', 'sale', 'buyer_choice', 'novelties', 'subcategory')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_photo')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="100" height="150">')
        else:
            return 'Фото не установлено'
    get_photo.short_description = 'Минимтюра'

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
