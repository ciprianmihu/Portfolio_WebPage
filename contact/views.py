from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from FinalProject.settings import ADMIN_USERNAME
from contact.forms import ContactForm
from userextend.models import UserExtend


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid() and not form.errors:
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            recipient = form.cleaned_data.get('email')
            try:
                # send_mail(subject, message, recipient, [settings.EMAIL_HOST_USER])
                send_mail(subject, message, recipient, [UserExtend.objects.get(username=ADMIN_USERNAME).email])
            except BadHeaderError:
                return HttpResponse("Invalid header found!")
            return redirect('success_view')
    return render(request, 'contact/contact.html', {'form': form})


def success_view(request):
    return render(request, 'contact/message_sent_confirmation.html')
