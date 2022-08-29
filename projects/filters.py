# pip install django_filter

import django_filters
# from django import forms

from projects.models import ProjectLogo


class ProjectsFilter(django_filters.FilterSet):
    project_name = django_filters.CharFilter(lookup_expr='icontains', label='Project name')
    logo_name = django_filters.CharFilter(lookup_expr='icontains', label='Logo name')
    project_description = django_filters.CharFilter(lookup_expr='icontains', label='Project description')

    class Meta:
        model = ProjectLogo
        fields = ['project_name', 'logo_name', 'project_description', 'service_name', 'ready_logo', 'client_name',
                  'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters['project_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter project name'})
        self.filters['logo_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter logo name'})
        self.filters['project_description'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter project description'})
        self.filters['service_name'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['ready_logo'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['client_name'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['status'].field.widget.attrs.update({'class': 'form-select'})
