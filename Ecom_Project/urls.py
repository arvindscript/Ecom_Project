from django.contrib import admin
from django.urls import path,include
from Ecom_App.views import Home  # ✅ Import views properly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', Home.as_view(), name='home'),
   
]
