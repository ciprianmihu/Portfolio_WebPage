from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    # class responsible for showing the page
    template_name = 'home/home.html'


def error_400(request, exception):
    # class responsible for showing the 400 error page
    return render(request, 'errors/400.html')


def error_403(request, exception):
    # class responsible for showing the 403 error page
    return render(request, 'errors/403.html')


def error_404(request, exception):
    # class responsible for showing the 404 error page
    return render(request, 'errors/404.html')


def error_500(request):
    # class responsible for showing the 500 error page
    return render(request, 'errors/500.html')
