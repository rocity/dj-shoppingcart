from django.contrib import admin

from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')

admin.site.register(Product, ProductAdmin)
