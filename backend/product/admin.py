from django.contrib import admin
from .models import Product, ProductCategory, ProductImage

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','status']
    search_fields = ['name']
    list_filter = ['status']
admin.site.register(ProductCategory,ProductCategoryAdmin)


# class ProductImagesInlines(admin.StackedInline):
    # model = ProductImage
    # extra = 0

class ProductImagesInlines(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','product_category','price','status']
    list_filter = ['product_category','status']
    search_fields = ['name','price']
    inlines = [ProductImagesInlines]

admin.site.register(Product,ProductAdmin)



