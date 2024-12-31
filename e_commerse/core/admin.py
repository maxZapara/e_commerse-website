from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'discount','available')
    list_filter = ('category','available')
    search_fields = ('title', 'description')
    list_editable=('price', 'discount', 'available')