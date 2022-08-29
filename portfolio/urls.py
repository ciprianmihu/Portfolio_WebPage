from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from portfolio import views

urlpatterns = [
    path('portfolio/', views.PortfolioListView.as_view(), name='portfolio'),
    path('create_portfolio_logo/', views.PortfolioCreateView.as_view(), name='create-portfolio-logo'),
    path('update_portfolio_logo/<int:pk>/', views.PortfolioUpdateView.as_view(), name='update-portfolio-logo'),
    path('detail_portfolio_logo/<int:pk>/', views.PortfolioDetailView.as_view(), name='detail-portfolio-logo'),
    path('delete_portfolio_logo/<int:pk>/', views.PortfolioDeleteView.as_view(), name='delete-portfolio-logo'),
    path('delete_portfolio_logo_modal/<int:pk>/', views.delete_portfolio_logo, name='delete-portfolio-logo-modal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
