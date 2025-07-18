from django.views.generic import TemplateView
from .models import Product,All_Product


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = Product.objects.all()[:6] 
        context['all_products'] = All_Product.objects.all()[:6]  # fix here

        return context
