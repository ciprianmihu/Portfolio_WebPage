from django.urls import path

from about import views

urlpatterns = [
    path('about/', views.AboutTemplateView.as_view(), name='about')
]
