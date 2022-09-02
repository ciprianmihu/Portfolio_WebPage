from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from projects.filters import ProjectsFilter
from projects.forms import ProjectLogoForm, ProjectLogoClientForm
from projects.models import ProjectLogo


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


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/create_project_logo.html'
    model = ProjectLogo
    form_class = ProjectLogoForm
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_project_logo = form.save(commit=False)
            new_project_logo.save()
            return redirect('projects')


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'projects/detail_project_logo.html'
    model = ProjectLogo


class ProjectActivityView(LoginRequiredMixin, DetailView):
    template_name = 'projects/activity_project_logo.html'
    model = ProjectLogo


class ProjectFilesView(LoginRequiredMixin, DetailView):
    template_name = 'projects/files_project_logo.html'
    model = ProjectLogo


class ProjectPaymentsView(LoginRequiredMixin, DetailView):
    template_name = 'projects/payments_project_logo.html'
    model = ProjectLogo


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/update_project_logo.html'
    model = ProjectLogo
    form_class = ProjectLogoForm
    success_url = reverse_lazy('projects')


class ProjectUpdateClientView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/update_project_logo.html'
    model = ProjectLogo
    form_class = ProjectLogoClientForm
    success_url = reverse_lazy('projects')


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
