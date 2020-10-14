from django.contrib import admin
from product.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('id','name', 'description','thumbnail', 'developer','technology_used', 'language')
