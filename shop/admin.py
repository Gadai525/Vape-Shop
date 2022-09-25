from django.contrib import admin
from django.utils.safestring import mark_safe


from shop.models import *



#-----------------------------------------------------------------------------------------

""" Продукт """
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'mini_description', 'description', 'product_characteristics', 'sale', 'buyer_choice', 'novelties', 'old_price', 'new_price', 'subcategory')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_photo')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="100" height="150">')
        else:
            return 'Фото не установлено'
    get_photo.short_description = 'Минимтюра'

class BrendsAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'get_photo')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="150" height="70">')
        else:
            return 'Фото не установлено'
    get_photo.short_description = 'Минимтюра'

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

class NicoboosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')

class FortressAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')

class GallaryAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_photo')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="100" height="150">')
        else:
            return 'Фото не установлено'
    get_photo.short_description = 'Минимтюра'

class TastesAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_photo', 'product')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="100" height="150">')
        else:
            return 'Фото не установлено'
    get_photo.short_description = 'Минимтюра'

class VolumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_at', 'text', 'slug', 'get_photo')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="100" height="150">')
        else:
            return 'Фото не установлено'
    get_photo.short_description = 'Минимтюра'

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brends, BrendsAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Nicobooster, NicoboosterAdmin)
admin.site.register(Fortress, FortressAdmin)
admin.site.register(Gallary, GallaryAdmin)
admin.site.register(Tastes, TastesAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(News, NewsAdmin)
