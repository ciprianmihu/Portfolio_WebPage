from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from projects import views

urlpatterns = [
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('create_project_logo/', views.ProjectCreateView.as_view(), name='create-project-logo'),
    path('detail_project_logo/<int:pk>/', views.ProjectDetailView.as_view(), name='detail-project-logo'),
    path('update_project_logo/<int:pk>/', views.ProjectUpdateView.as_view(), name='update-project-logo'),
    path('update_project_client/<int:pk>/', views.ProjectClientUpdateView.as_view(), name='update-project-client'),
    path('delete_project_logo/<int:pk>/', views.ProjectDeleteView.as_view(), name='delete-project-logo'),
    path('delete_project_logo_modal/<int:pk>/', views.delete_project_logo, name='delete-project-logo-modal'),
    path('activity_project_logo/<int:pk>/', views.ProjectActivityView.as_view(), name='activity-project-logo'),
    path('payments_project_logo/<int:pk>/', views.ProjectPaymentsView.as_view(), name='payments-project-logo'),
    path('files_project_logo/<int:pk>/', views.ProjectFilesView.as_view(), name='files-project-logo'),
    path('create_project_logo_files/<int:pk>/', views.ProjectFilesCreateView.as_view(),
         name='create-project-logo-files'),
    path('create_project_logo_files_c/<int:pk>/', views.ProjectFilesClientCreateView.as_view(),
         name='create-project-logo-files-c'),
    path('project/<int:project_id>/detail_project_logo_files/<int:pk>/', views.ProjectFilesDetailView.as_view(),
         name='detail-project-logo-files'),
    path('update_project_logo_files/<int:pk>/', views.ProjectFilesUpdateView.as_view(),
         name='update-project-logo-files'),
    path('update_project_logo_files_c/<int:pk>/', views.ProjectFilesClientUpdateView.as_view(),
         name='update-project-logo-files-c'),
    path('project/<int:project_id>/delete_project_logo_file_modal/<int:pk>/', views.delete_project_file,
         name='delete-project-logo-file-modal'),
    path('create_project_logo_comment_file/<int:pk>/', views.ProjectFilesCommentCreateView.as_view(),
         name='create-project-logo-files-comment'),
    path('create_project_logo_message/<int:pk>/', views.ProjectMessageCreateView.as_view(),
         name='create-project-logo-message'),
    path('create_project_logo_payment/<int:pk>/', views.ProjectPaymentCreateView.as_view(),
         name='create-project-logo-payment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
