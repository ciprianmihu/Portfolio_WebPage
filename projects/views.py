from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from FinalProject.settings import EMAIL_HOST_USER
from projects.filters import ProjectsFilter
from projects.forms import ProjectLogoForm, ProjectLogoClientForm, ProjectFileForm, ProjectFileUpdateForm, \
    CommentProjectFileForm
from projects.models import ProjectLogo, ProjectFile, CommentProjectFile, ProjectActivity


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/create_project_logo.html'
    model = ProjectLogo
    form_class = ProjectLogoForm
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_project_logo = form.save(commit=False)
            new_project_logo.save()
            ProjectActivity.objects.create(
                project=new_project_logo,
                message='Your project has been created'
            )

            subject = 'New project created.'
            message = None
            html_message1 = render_to_string('email_project.html', {'new_project_logo': new_project_logo})

            send_mail(subject, message, EMAIL_HOST_USER, [self.request.user.email], html_message=html_message1)

            return redirect('projects')


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'projects/projects.html'
    model = ProjectLogo
    context_object_name = 'all_projects'

    def get_queryset(self):
        queryset = super(ProjectListView, self).get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        filter_queryset = queryset.filter(client_name=self.request.user)
        return filter_queryset

    def get_context_data(self, **kwargs):
        data = super(ProjectListView, self).get_context_data(**kwargs)

        projects = ProjectLogo.objects.all()
        my_filter = ProjectsFilter(self.request.GET, queryset=projects)
        if self.request.user.is_superuser:
            data['count_all'] = projects.count()
            data['count_draft'] = projects.filter(status='Draft').count()
            data['count_started'] = projects.filter(status='Started').count()
            data['count_completed'] = projects.filter(status='Completed').count()
            data['count_canceled'] = projects.filter(status='Canceled').count()
        else:
            data['count_all'] = projects.filter(client_name=self.request.user).count()
            data['count_draft'] = projects.filter(status='Draft', client_name=self.request.user).count()
            data['count_started'] = projects.filter(status='Started', client_name=self.request.user).count()
            data['count_completed'] = projects.filter(status='Completed', client_name=self.request.user).count()
            data['count_canceled'] = projects.filter(status='Canceled', client_name=self.request.user).count()
        if self.request.user.is_superuser:
            data['all_projects'] = my_filter.qs
            data['my_filter'] = my_filter
        else:
            data['all_projects'] = self.get_queryset()

        return data


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'projects/detail_project_logo.html'
    model = ProjectLogo


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/update_project_logo.html'
    model = ProjectLogo
    form_class = ProjectLogoForm

    def get_success_url(self):
        return reverse('detail-project-logo', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_project_logo = form.save(commit=False)
            new_project_logo.save()
            ProjectActivity.objects.update(
                project=new_project_logo,
                message='Your project has been updated'
            )

            subject = 'Your project has been updated.'
            message = None
            html_message1 = render_to_string('email_project_update.html', {'new_project_logo': new_project_logo})

            if self.request.user.is_superuser:
                send_mail(subject, message, EMAIL_HOST_USER, [self.request.user.email], html_message=html_message1)
            else:
                send_mail(subject, message, EMAIL_HOST_USER, [self.request.user.email], html_message=html_message1)

            return redirect('projects')


class ProjectClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/update_project_logo.html'
    model = ProjectLogo
    form_class = ProjectLogoClientForm

    def get_success_url(self):
        return reverse('detail-project-logo', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_project_logo = form.save(commit=False)
            new_project_logo.save()
            ProjectActivity.objects.create(
                project=new_project_logo,
                message='Your project has been updated'
            )

            subject = 'Your project has been updated.'
            message = None
            html_message1 = render_to_string('email_project_update.html', {'new_project_logo': new_project_logo})

            if self.request.user.is_superuser:
                send_mail(subject, message, EMAIL_HOST_USER, [self.request.user.email], html_message=html_message1)
            else:
                send_mail(subject, message, EMAIL_HOST_USER, [self.request.user.email], html_message=html_message1)

            return redirect('projects')


class ProjectDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'projects/delete_project_logo.html'
    model = ProjectLogo
    success_url = reverse_lazy('projects')
    permission_required = 'portfolio.delete_projectlogo'


@login_required
@permission_required('portfolio.delete_projectlogo')
def delete_project_logo(request, pk):
    ProjectLogo.objects.filter(id=pk).delete()

    return redirect('projects')


class ProjectFilesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/files/create_project_logo_file.html'
    model = ProjectFile
    form_class = ProjectFileForm

    def get_success_url(self):
        return reverse('files-project-logo', kwargs={'pk': self.object.project.id})

    # def form_valid(self, form):
    #     if form.is_valid() and not form.errors:
    #         new_project_file = form.save(commit=False)
    #         new_project_file.save()
    #
    #         return redirect(reverse('files-project-logo', kwargs={'pk': self.object.id}))


class ProjectFilesView(LoginRequiredMixin, DetailView):
    template_name = 'projects/files/files_project_logo.html'
    model = ProjectLogo

    def get_context_data(self, **kwargs):
        status = self.request.GET.get('status')
        data = super(ProjectFilesView, self).get_context_data(**kwargs)
        all_files = ProjectFile.objects.filter(project=self.kwargs.get('pk'))
        if status:
            files = ProjectFile.objects.filter(project=self.kwargs.get('pk')).filter(status=status)
        else:
            files = ProjectFile.objects.filter(project=self.kwargs.get('pk'))
        data['files'] = files
        data['count_all'] = all_files.count()
        data['count_reference'] = all_files.filter(status='Reference').count()
        data['count_in_progress'] = all_files.filter(status='In progress').count()
        data['count_declined'] = all_files.filter(status='Declined').count()
        data['count_final'] = all_files.filter(status='Final').count()

        return data


class ProjectFilesDetailView(LoginRequiredMixin, DetailView):
    template_name = 'projects/files/detail_project_logo_file.html'
    model = ProjectFile

    def get_context_data(self, **kwargs):
        data = super(ProjectFilesDetailView, self).get_context_data(**kwargs)
        comments = CommentProjectFile.objects.filter(project_file=self.kwargs.get('pk'))
        data['comments'] = comments

        return data


class ProjectFilesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/files/update_project_logo_file.html'
    model = ProjectFile
    form_class = ProjectFileForm

    def get_success_url(self):
        return reverse('files-project-logo', kwargs={'pk': self.object.project.id})


class ProjectFilesClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/files/update_project_logo_file.html'
    model = ProjectFile
    form_class = ProjectFileUpdateForm

    def get_success_url(self):
        return reverse('files-project-logo', kwargs={'pk': self.object.project.id})


class ProjectFilesCommentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/comments/create_project_logo_file_comment.html'
    model = CommentProjectFile
    form_class = CommentProjectFileForm

    def get_context_data(self, **kwargs):
        data = super(ProjectFilesCommentCreateView, self).get_context_data(**kwargs)
        project_file = ProjectFile.objects.filter(project=self.kwargs.get('pk'))
        data['project_file'] = project_file
        projects = ProjectLogo.objects.all()
        if self.request.user.is_superuser:
            data['projects'] = projects
        else:
            data['projects'] = projects.filter(client_name=self.request.user)

        return data

    def get_success_url(self):
        return reverse('files-project-logo', kwargs={'pk': self.object.id})


class ProjectActivityView(LoginRequiredMixin, DetailView):
    template_name = 'projects/activity/activity_project_logo.html'
    model = ProjectLogo

    def get_context_data(self, **kwargs):
        data = super(ProjectActivityView, self).get_context_data(**kwargs)
        activities = ProjectActivity.objects.filter(project=self.kwargs.get('pk'))
        data['activities'] = activities

        return data


class ProjectPaymentsView(LoginRequiredMixin, DetailView):
    template_name = 'projects/payments/payments_project_logo.html'
    model = ProjectLogo
