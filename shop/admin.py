from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget


from shop.models import *



#-----------------------------------------------------------------------------------------

class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'



""" Продукт """
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'mini_description', 'description', 'product_characteristics', 'sale', 'buyer_choice', 'novelties', 'old_price', 'new_price', 'subcategory', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'get_photo')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="100" height="150">')
        else:
            return 'Фото не установлено'
    get_photo.short_description = 'Минимтюра'

class BrendsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'get_photo')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" width="150" height="70">')
        else:
            return 'Фото не установлено'
    get_photo.short_description = 'Минимтюра'

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'category')

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

class Bonuses_giftsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Bonuses_gifts
        fields = '__all__'

class Bonuses_giftsAdmin(admin.ModelAdmin):
    form = Bonuses_giftsAdminForm
    list_display = ('text',)

class DeliveryAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Delivery
        fields = '__all__'

class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display = ('text',)


class PaymentAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    list_display = ('text',)


class How_to_orderAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = How_to_order
        fields = '__all__'

class How_to_orderAdmin(admin.ModelAdmin):
    form = How_to_orderAdminForm
    list_display = ('text',)


class GuaranteesAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Guarantees
        fields = '__all__'

class GuaranteesAdmin(admin.ModelAdmin):
    form = GuaranteesAdminForm
    list_display = ('text',)


class MainPageAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = MainPage
        fields = '__all__'

class MainPageAdmin(admin.ModelAdmin):
    form = MainPageAdminForm
    list_display = ('text',)



class HelpAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Help
        fields = '__all__'

class HelpAdmin(admin.ModelAdmin):
    form = HelpAdminForm
    list_display = ('title', 'text')



class StockAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Stock
        fields = '__all__'

class StockAdmin(admin.ModelAdmin):
    form = StockAdminForm
    list_display = ('title', 'text')




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
admin.site.register(Bonuses_gifts, Bonuses_giftsAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(How_to_order, How_to_orderAdmin)
admin.site.register(Guarantees, GuaranteesAdmin)
admin.site.register(MainPage, MainPageAdmin)
admin.site.register(Help, HelpAdmin)
admin.site.register(Stock, StockAdmin)
