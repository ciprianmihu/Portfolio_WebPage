from django.urls import path

from contact import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('success_view/', views.success_view, name='success_view')
]