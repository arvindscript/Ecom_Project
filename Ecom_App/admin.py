from django.contrib import admin
from .models import Product,All_Product,Latest_Product,Blog_Product,Festival_Deals

admin.site.register(Product)
admin.site.register(All_Product)
admin.site.register(Latest_Product)
admin.site.register(Blog_Product)
admin.site.register(Festival_Deals)