from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from services.forms import ServiceForm
from services.models import ServiceLogo


class ServiceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'services/create_service.html'
    model = ServiceLogo
    form_class = ServiceForm
    success_url = reverse_lazy('services')
    permission_required = 'services.add_servicelogo'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_service_logo = form.save(commit=False)
            new_service_logo.save()
            return redirect('services')


class ServiceListView(LoginRequiredMixin, ListView):
    template_name = 'services/services.html'
    model = ServiceLogo
    context_object_name = 'all_services'


class ServiceDetailView(LoginRequiredMixin, DetailView):
    template_name = 'services/detail_service.html'
    model = ServiceLogo


class ServiceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'services/update_service.html'
    model = ServiceLogo
    form_class = ServiceForm
    permission_required = 'services.change_servicelogo'

    def get_success_url(self):
        return reverse('detail-service-logo', kwargs={'pk': self.object.id})


class ServiceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'services/delete_service.html'
    model = ServiceLogo
    success_url = reverse_lazy('services')
    permission_required = 'services.delete_servicelogo'


@login_required
@permission_required('services.delete_servicelogo')
def delete_service_logo(request, pk):
    ServiceLogo.objects.filter(id=pk).delete()

    return redirect('services')
