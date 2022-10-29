from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from portfolio.forms import PortfolioLogoForm
from portfolio.models import PortfolioLogo


class PortfolioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    # class responsible for creating a portfolio logo
    template_name = 'portfolio/create_portfolio.html'
    model = PortfolioLogo
    form_class = PortfolioLogoForm
    success_url = reverse_lazy('portfolio')
    permission_required = 'portfolio.add_portfoliologo'

    def form_valid(self, form):
        # method responsible for saving the form
        if form.is_valid() and not form.errors:
            new_portfolio_logo = form.save(commit=False)
            new_portfolio_logo.save()
            return redirect('portfolio')


class PortfolioListView(ListView):
    # class responsible for showing all logos
    template_name = 'portfolio/portfolio.html'
    model = PortfolioLogo
    context_object_name = 'all_portfolio_logos'
    paginate_by = 8


class PortfolioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    # class responsible for updating the logos
    template_name = 'portfolio/update_portfolio.html'
    model = PortfolioLogo
    form_class = PortfolioLogoForm
    permission_required = 'portfolio.change_portfoliologo'

    def get_success_url(self):
        # method responsible for returning after the logo creation
        return reverse('detail-portfolio', kwargs={'pk': self.object.id})


class PortfolioDetailView(DetailView):
    # class responsible for showing the logo details
    template_name = 'portfolio/detail_portfolio.html'
    model = PortfolioLogo

    def get_context_data(self, **kwargs):
        # method responsible for the navigation to next and previous logo
        data = super(PortfolioDetailView, self).get_context_data(**kwargs)
        logo_ids = list(PortfolioLogo.objects.all().values_list('pk', flat=True))
        data['previous_logo_id'] = logo_ids[logo_ids.index(self.object.id) - 1]
        try:
            data['next_logo_id'] = logo_ids[logo_ids.index(self.object.id) + 1]
        except IndexError:
            data['next_logo_id'] = logo_ids[0]

        return data


@login_required
@permission_required('portfolio.delete_portfoliologo')
def delete_portfolio_logo(request, pk):
    # function responsible for deleting a logo
    PortfolioLogo.objects.filter(id=pk).delete()

    return redirect('portfolio')
