from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

class CustomLoginView(LoginView):
    # Your custom implementation for login view
    template_name = 'home/login.html'  # Example: specify a custom template for login

class CustomLogoutView(LogoutView):
    # Your custom implementation for logout view
    template_name = 'home/home.html'  # Example: specify a custom template for logout

def home(request):
    # Your home view logic
    return render(request, 'home/home.html')

def signup(request):
    # Your signup view logic
    return render(request, 'home/signup.html')
