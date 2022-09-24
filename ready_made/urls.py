from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from ready_made import views

urlpatterns = [
    path('ready_made/', views.ReadyMadeListView.as_view(), name='ready-made'),
    path('create_ready/', views.ReadeMadeCreateView.as_view(), name='create-ready'),
    path('update_ready/<int:pk>/', views.ReadeMadeUpdateView.as_view(), name='update-ready'),
    path('detail_ready/<int:pk>/', views.ReadyMadeDetailView.as_view(), name='detail-ready'),
    path('delete_ready/<int:pk>/', views.delete_ready_logo, name='delete-ready'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
