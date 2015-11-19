from django.contrib import admin
from models import Product, Category, Item, Phone


class ProductInline(admin.StackedInline):
    model = Product
    verbose_name = u'Product'
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    inlines = (ProductInline,)


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name', 'category')
    list_display = ('name', 'category', 'price')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Item)
admin.site.register(Phone)