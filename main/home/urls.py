from django.urls import path
from home.views import CustomLoginView, CustomLogoutView, home, signup

urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]
