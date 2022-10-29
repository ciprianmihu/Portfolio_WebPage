from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from services.forms import ServiceForm
from services.models import ServiceLogo


class ServiceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # class responsible for creating a service
    template_name = 'services/create_service.html'
    model = ServiceLogo
    form_class = ServiceForm
    success_url = reverse_lazy('services')
    permission_required = 'services.add_servicelogo'

    def form_valid(self, form):
        # method responsible for saving the form
        if form.is_valid() and not form.errors:
            new_service_logo = form.save(commit=False)
            new_service_logo.save()
            return redirect('services')


class ServiceListView(LoginRequiredMixin, ListView):
    # class responsible for showing all services
    template_name = 'services/services.html'
    model = ServiceLogo
    context_object_name = 'all_services'


class ServiceDetailView(LoginRequiredMixin, DetailView):
    # class responsible for showing the service details
    template_name = 'services/detail_service.html'
    model = ServiceLogo

    def get_context_data(self, **kwargs):
        # method responsible for the navigation to next and previous service
        data = super(ServiceDetailView, self).get_context_data(**kwargs)
        service_ids = list(ServiceLogo.objects.all().values_list('pk', flat=True))
        data['previous_service_id'] = service_ids[service_ids.index(self.object.id) - 1]
        try:
            data['next_service_id'] = service_ids[service_ids.index(self.object.id) + 1]
        except IndexError:
            data['next_service_id'] = service_ids[0]

        return data


class ServiceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    # class responsible for updating the services
    template_name = 'services/update_service.html'
    model = ServiceLogo
    form_class = ServiceForm
    permission_required = 'services.change_servicelogo'

    def get_success_url(self):
        # method responsible for returning after the service creation
        return reverse('detail-service', kwargs={'pk': self.object.id})


@login_required
@permission_required('services.delete_servicelogo')
def delete_service_logo(request, pk):
    # function responsible for deleting a service
    ServiceLogo.objects.filter(id=pk).delete()

    return redirect('services')
