from django.contrib import admin

from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    search_fields = ('title', 'description')

admin.site.register(Product, ProductAdmin)
