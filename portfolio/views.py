from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from portfolio.forms import PortfolioLogoForm
from portfolio.models import PortfolioLogo


class PortfolioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'portfolio/create_portfolio_logo.html'
    model = PortfolioLogo
    form_class = PortfolioLogoForm
    success_url = reverse_lazy('portfolio')
    permission_required = 'portfolio.add_portfoliologo'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_portfolio_logo = form.save(commit=False)
            new_portfolio_logo.save()
            return redirect('portfolio')


class PortfolioListView(ListView):
    template_name = 'portfolio/portfolio.html'
    model = PortfolioLogo
    context_object_name = 'all_portfolio_logos'
    paginate_by = 8


class PortfolioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'portfolio/update_portfolio_logo.html'
    model = PortfolioLogo
    form_class = PortfolioLogoForm
    permission_required = 'portfolio.change_portfoliologo'

    def get_success_url(self):
        return reverse('detail-portfolio-logo', kwargs={'pk': self.object.id})


class PortfolioDetailView(DetailView):
    template_name = 'portfolio/detail_portfolio_logo.html'
    model = PortfolioLogo

    def get_context_data(self, **kwargs):
        data = super(PortfolioDetailView, self).get_context_data(**kwargs)
        logo_ids = PortfolioLogo.objects.all().values_list('pk', flat=True)
        data['logo_ids'] = logo_ids

        return data


class PortfolioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'portfolio/delete_portfolio_logo.html'
    model = PortfolioLogo
    success_url = reverse_lazy('portfolio')
    permission_required = 'portfolio.delete_portfoliologo'


@login_required
@permission_required('portfolio.delete_portfoliologo')
def delete_portfolio_logo(request, pk):
    PortfolioLogo.objects.filter(id=pk).delete()

    return redirect('portfolio')
