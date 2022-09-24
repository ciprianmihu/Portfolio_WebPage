from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from ready_made import views

urlpatterns = [
    path('ready_made/', views.ReadyMadeListView.as_view(), name='ready-made'),
    path('create_ready_logo/', views.ReadeMadeCreateView.as_view(), name='create-ready-logo'),
    path('update_ready_logo/<int:pk>/', views.ReadeMadeUpdateView.as_view(), name='update-ready-logo'),
    path('detail_ready_logo/<int:pk>/', views.ReadyMadeDetailView.as_view(), name='detail-ready-logo'),
    path('delete_ready_logo_modal/<int:pk>/', views.delete_ready_logo, name='delete-ready-logo-modal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
