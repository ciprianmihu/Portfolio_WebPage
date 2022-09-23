from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from projects import views

urlpatterns = [
                  path('projects/', views.ProjectListView.as_view(), name='projects'),
                  path('create_project/', views.ProjectCreateView.as_view(), name='create-project'),
                  path('detail_project/<int:pk>/', views.ProjectDetailView.as_view(), name='detail-project'),
                  path('update_project/<int:pk>/', views.ProjectUpdateView.as_view(), name='update-project'),
                  path('update_project_client/<int:pk>/', views.ProjectClientUpdateView.as_view(),
                       name='update-project-client'),
                  path('delete_project_modal/<int:pk>/', views.delete_project_logo, name='delete-project-modal'),
                  path('project_activity/<int:pk>/', views.ProjectActivityView.as_view(), name='project-activity'),
                  path('project_payments/<int:pk>/', views.ProjectPaymentsView.as_view(), name='project-payments'),
                  path('project_files/<int:pk>/', views.ProjectFilesView.as_view(), name='project-files'),
                  path('create_project_file/<int:pk>/', views.ProjectFilesCreateView.as_view(),
                       name='create-project-file'),
                  path('create_project_file_c/<int:pk>/', views.ProjectFilesClientCreateView.as_view(),
                       name='create-project-file-c'),
                  path('project/<int:project_id>/detail_project_file/<int:pk>/', views.ProjectFilesDetailView.as_view(),
                       name='detail-project-file'),
                  path('update_project_file/<int:pk>/', views.ProjectFilesUpdateView.as_view(),
                       name='update-project-file'),
                  path('update_project_file_c/<int:pk>/', views.ProjectFilesClientUpdateView.as_view(),
                       name='update-project-file-c'),
                  path('project/<int:project_id>/delete_project_file_modal/<int:pk>/', views.delete_project_file,
                       name='delete-project-file-modal'),
                  path('create_project_file_comment/<int:pk>/', views.ProjectFilesCommentCreateView.as_view(),
                       name='create-project-file-comment'),
                  path('create_project_message/<int:pk>/', views.ProjectMessageCreateView.as_view(),
                       name='create-project-message'),
                  path('create_project_payment/<int:pk>/', views.ProjectPaymentCreateView.as_view(),
                       name='create-project-payment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
