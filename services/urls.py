from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from services import views

urlpatterns = [
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('create_service_logo/', views.ServiceCreateView.as_view(), name='create-service-logo'),
    path('detail_service_logo/<int:pk>/', views.ServiceDetailView.as_view(), name='detail-service-logo'),
    path('update_service_logo/<int:pk>/', views.ServiceUpdateView.as_view(), name='update-service-logo'),
    path('delete_service_logo_modal/<int:pk>/', views.delete_service_logo, name='delete-service-logo-modal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
