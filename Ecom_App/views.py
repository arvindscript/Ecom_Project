
# views.py
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from .models import Product, All_Product, Latest_Product,Blog_Product
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

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
#             return redirect('home')  # Ensure 'home' is defined in urls.py with name='home'
#         else:
#             messages.error(request, 'Invalid email or password')
#             return render(request, self.template_name)  # ✅ Correct template re-render

# class CreateInView(TemplateView):
#     template_name = 'create.html'



# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.views import View
# from .forms import SignUpForm  

class SignInView(View):
    template_name = 'signin.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid email or password')
        return render(request, self.template_name)

class CreateInView(View):  
    template_name = 'create.html'

    def get(self, request):
        form = SignInView()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignInView(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})
