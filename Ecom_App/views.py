
# from django.views.generic import TemplateView


# class Home(TemplateView):
#     template_name = 'home.html'
# from django.views.generic import TemplateView

# class Home(TemplateView):
#     template_name = 'home.html'
  

from django.views.generic import TemplateView
from .models import Product,All_Product

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = Product.objects.all()[:6] 
        print('context') # Limit to 6 latest products
        return context

    def get_content_data(self, **kwargs):
        content = super().get_content_data(**kwargs)

        content['All_products'] = All_Product.objects.all()[:6] 
        print('content') # Limit to 6 latest products
        return content
