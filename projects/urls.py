from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from projects import views

urlpatterns = [
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('create_project_logo/', views.ProjectCreateView.as_view(), name='create-project-logo'),
    path('detail_project_logo/<int:pk>/', views.ProjectDetailView.as_view(), name='detail-project-logo'),
    path('activity_project_logo/<int:pk>/', views.ProjectActivityView.as_view(), name='activity-project-logo'),
    path('files_project_logo/<int:pk>/', views.ProjectFilesView.as_view(), name='files-project-logo'),
    path('payments_project_logo/<int:pk>/', views.ProjectPaymentsView.as_view(), name='payments-project-logo'),
    path('update_project_logo/<int:pk>/', views.ProjectUpdateView.as_view(), name='update-project-logo'),
    path('delete_project_logo/<int:pk>/', views.ProjectDeleteView.as_view(), name='delete-project-logo'),
    path('delete_project_logo_modal/<int:pk>/', views.delete_project_logo, name='delete-project-logo-modal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
