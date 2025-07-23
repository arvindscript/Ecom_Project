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
from django.views import View
from django.shortcuts import render, redirect
from .models import Product, All_Product, Latest_Product,Blog_Product
from django.contrib.auth import authenticate, login
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[:6] 
        context['all_products'] = All_Product.objects.all()[:6]
        context['latest_products'] = Latest_Product.objects.all() # fixed here
        context['blog_products'] = Blog_Product.objects.all()[:3]
        return context
    

# class SignInView(TemplateView):
#     template_name = 'signin.html'

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Make sure 'home' is a named URL in your urls.py
#         else:
#             messages.error(request, 'Invalid email or password')
#             return render(request, self.create.html)
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

class SignInView(TemplateView):
    template_name = 'signin.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Ensure 'home' is defined in urls.py with name='home'
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, self.template_name)  # ✅ Correct template re-render
