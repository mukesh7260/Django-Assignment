from django.contrib import admin

from product.models import ProductMainModel , ProductImageModel

@admin.register(ProductMainModel)
class ProductMainModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','descriptions','unique_id','price']
    
@admin.register(ProductImageModel)
class ProductImageModel(admin.ModelAdmin):
    list_display = ['id','image','product']