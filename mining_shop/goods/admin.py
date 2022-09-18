from django.contrib import admin
from goods.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Product, ProductAdmin)
