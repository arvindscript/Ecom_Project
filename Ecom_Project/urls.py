from django.contrib import admin
from django.urls import path
from Ecom_App.views import HomePageView,SignInView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('signin/', SignInView.as_view(), name='signin'), 
    #  path('signup/',SignInView.as_view(), name='signin'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
