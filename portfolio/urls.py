from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from portfolio import views

urlpatterns = [
    path('portfolio/', views.PortfolioListView.as_view(), name='portfolio'),
    path('create_portfolio/', views.PortfolioCreateView.as_view(), name='create-portfolio'),
    path('update_portfolio/<int:pk>/', views.PortfolioUpdateView.as_view(), name='update-portfolio'),
    path('detail_portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='detail-portfolio'),
    path('delete_portfolio/<int:pk>/', views.delete_portfolio_logo, name='delete-portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
