
from django.views.generic import TemplateView
# from main_app.views import Home 

class Home(TemplateView):
    template_name = 'home.html'
