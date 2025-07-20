# from django.views.generic import TemplateView
# from .models import Product,All_Product,Latest_Product


# class HomePageView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context['products'] = Product.objects.all()[:6] 
#         context['all_products'] = All_Product.objects.all()[:6]  # fix here
#         context['lates_products'] = Latest_Product.objects.all()[:6]   
#         return context

# views.py
from django.views.generic import TemplateView
from .models import Product, All_Product, Latest_Product,Blog_Product

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:6] 
        context['all_products'] = All_Product.objects.all()[:6]
        context['latest_products'] = Latest_Product.objects.all() # fixed here
        context['blog_products'] = Blog_Product.objects.all()[:3]
        return context
