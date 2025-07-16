
# from django.views.generic import TemplateView


# class Home(TemplateView):
#     template_name = 'home.html'
# from django.views.generic import TemplateView

# class Home(TemplateView):
#     template_name = 'home.html'
  

from django.views.generic import TemplateView
from .models import Product

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = Product.objects.all()[:6] 
        print('context') # Limit to 6 latest products
        return context
