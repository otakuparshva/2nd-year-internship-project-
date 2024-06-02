from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

# You can create custom login and logout views if you want to add custom context or behavior
class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'  # Define your login template here

class CustomLogoutView(auth_views.LogoutView):
    next_page = 'home'  # Redirect to the home page after logout

# Optionally, you can define additional views here if needed
