from django.contrib import admin
from  product.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['productName','productDesc','producter','create_time','id']
    admin.site.register(Product)



