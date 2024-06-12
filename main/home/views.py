# views.py (main)
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm

class CustomLoginView(LoginView):
    template_name = 'home/login.html'  # Adjust the template path if needed

class CustomLogoutView(LogoutView):
    pass

def home(request):
    return render(request, 'home/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process form data
            pass
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})
