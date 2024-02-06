from django.contrib import admin
from .models import product

# Register your models here.

class serviceAdmin(admin.ModelAdmin):
    list_display=('product_icon', 'product_title', 'product_image', 'product_link','product_des','upload_product')

admin.site.register(product, serviceAdmin)