from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from FinalProject.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm, UserExtendUpdateForm, UserExtendUpdateBioForm
from userextend.models import UserExtend, UserProfile


class UserExtendCreateView(CreateView):
    # class responsible for creating a user
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # method responsible for saving the form
        if form.is_valid() and not form.errors:
            new_user = form.save()
            UserProfile.objects.create(
                user=new_user
            )

            subject = 'Create a new account'
            message = None
            html_message1 = render_to_string('emails/email.html', {'new_user': new_user})

            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email], html_message=html_message1)

            return redirect('login')


class UserExtendProfileView(LoginRequiredMixin, DetailView):
    # class responsible for showing the user detail
    template_name = 'userextend/profile_user.html'
    model = UserExtend

    def get_queryset(self):
        # method responsible for filtering to the current user
        queryset = super(UserExtendProfileView, self).get_queryset().filter(id=self.request.user.id)

        return queryset


class UserExtendUpdateView(LoginRequiredMixin, UpdateView):
    # class responsible for updating the user profile
    template_name = 'userextend/update_user.html'
    model = UserExtend
    form_class = UserExtendUpdateForm

    def get_success_url(self):
        # method responsible for returning after the update
        return reverse('profile-user', kwargs={'pk': self.request.user.id})


class UserExtendUpdateBioView(LoginRequiredMixin, UpdateView):
    # class responsible for updating the user bio
    template_name = 'userextend/update_user_bio.html'
    model = UserProfile
    form_class = UserExtendUpdateBioForm

    def get_success_url(self):
        # method responsible for returning after the update
        return reverse('profile-user', kwargs={'pk': self.request.user.id})


@login_required
def inactive_user(request, pk):
    # function responsible for deactivating an user
    UserExtend.objects.filter(id=pk).update(active=False)

    return redirect('detail-user')


@login_required
def active_user(request, pk):
    # function responsible for activating an user
    UserExtend.objects.filter(id=pk).update(active=True)

    return redirect('detail-user')
