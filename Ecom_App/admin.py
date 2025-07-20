from django.contrib import admin
from .models import Product,All_Product,Latest_Product,Blog_Product

admin.site.register(Product)
admin.site.register(All_Product)
admin.site.register(Latest_Product)
admin.site.register(Blog_Product)