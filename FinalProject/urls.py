"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import path, include

from userextend.forms import AuthenticationLoginForm, PasswordChangeFormExtend, PasswordResetFormExtend, \
    SetPasswordFormExtend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('about.urls')),
    path('', include('portfolio.urls')),
    path('', include('ready_made.urls')),
    path('', include('userextend.urls')),
    path('', include('contact.urls')),
    path('', include('services.urls')),
    path('', include('projects.urls')),
    path('login/', LoginView.as_view(form_class=AuthenticationLoginForm), name='login'),
    path('password_change/', PasswordChangeView.as_view(form_class=PasswordChangeFormExtend), name='password_change'),
    path('password_reset/', PasswordResetView.as_view(form_class=PasswordResetFormExtend), name='password_reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(form_class=SetPasswordFormExtend),
         name='password_reset_confirm'),
    path('', include('django.contrib.auth.urls')),
    # path('oauth/', include('social_django.urls', namespace='social')),
]
