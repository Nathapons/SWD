from django.contrib import admin
from . import models


class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_type',
        'name',
        'price',
        'unit',
        'created_on',
        'updated_on'
    ]
    search_fields = ['name']
    list_filter = ['created_on', 'updated_on']


admin.site.register(models.ProductsModel, ProductsAdmin)
