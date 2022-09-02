from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from ready_made.forms import ReadyMadeLogoForm
from ready_made.models import ReadyLogo


class ReadeMadeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'ready_made/create_ready_logo.html'
    model = ReadyLogo
    form_class = ReadyMadeLogoForm
    success_url = reverse_lazy('ready-made')
    permission_required = 'ready_made.add_readylogo'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_ready_logo = form.save(commit=False)
            new_ready_logo.save()
            return redirect('ready-made')


class ReadyMadeListView(ListView):
    template_name = 'ready_made/ready_made.html'
    model = ReadyLogo
    context_object_name = "all_ready_logos"
    paginate_by = 8


class ReadeMadeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'ready_made/update_ready_logo.html'
    model = ReadyLogo
    form_class = ReadyMadeLogoForm
    permission_required = 'ready_made.change_readylogo'

    def get_success_url(self):
        return reverse('detail-ready-logo', kwargs={'pk': self.object.id})


class ReadyMadeDetailView(DetailView):
    template_name = 'ready_made/detail_ready_logo.html'
    model = ReadyLogo


class ReadyMadeDeleteVIew(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'ready_made/delete_ready_logo.html'
    model = ReadyLogo
    success_url = reverse_lazy('ready-made')
    permission_required = 'ready_made.delete_readylogo'


@login_required
@permission_required('ready_made.delete_readylogo')
def delete_ready_logo(request, pk):
    ReadyLogo.objects.filter(id=pk).delete()

    return redirect('ready-made')

