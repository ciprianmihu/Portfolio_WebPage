from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from userextend import views

urlpatterns = [
    path('create_user/', views.UserExtendCreateView.as_view(), name='create-user'),
    path('profile_user/', views.UserExtendProfileView.as_view(), name='profile-user'),
    path('update_user/<int:pk>/', views.UserExtendUpdateView.as_view(), name='update-user'),
    path('inactive_user/<int:pk>/', views.inactive_user, name='inactive-user'),
    path('active_user/<int:pk>/', views.active_user, name='active-user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)