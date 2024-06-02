from django.contrib import admin
from django.urls import path, include
from home.views import CustomLoginView, CustomLogoutView, home, signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('allauth.urls')),  # Add this line
    path('social-auth/', include('social_django.urls', namespace='social')),  # Add this line
]
