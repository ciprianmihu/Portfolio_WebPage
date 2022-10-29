from django.shortcuts import render
from django.views.generic import TemplateView


class AboutTemplateView(TemplateView):
    # class responsible for showing the page
    template_name = 'about/about.html'
