from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from ready_made.models import ReadyLogo
from services.models import ServiceLogo
from userextend.models import UserExtend


class ProjectLogo(models.Model):
    project_name = models.CharField(max_length=100)
    logo_name = models.CharField(max_length=100)
    logo_slogan = models.CharField(max_length=100, blank=True)
    company_description = models.TextField(max_length=3000, blank=True)
    company_industry = models.CharField(max_length=100, blank=True)
    logo_colors = models.TextField(max_length=1000, blank=True)
    service_name = models.ForeignKey(ServiceLogo, on_delete=models.CASCADE, null=True, blank=True)
    ready_logo = models.ForeignKey(ReadyLogo, on_delete=models.CASCADE, null=True, blank=True)
    client_name = models.ForeignKey(UserExtend, on_delete=models.CASCADE, null=True)
    project_description = models.TextField(max_length=1000)
    optional_project_image_1 = models.ImageField(upload_to='projects/', null=True, blank=True)
    other_notes = models.TextField(max_length=1000, blank=True)
    status_options = (('Draft', 'Draft'), ('Started', 'Started'), ('Completed', 'Completed'), ('Canceled', 'Canceled'))
    status = models.CharField(max_length=9, choices=status_options, null=True)
    classic_or_modern = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    mature_or_youthful = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    feminine_or_masculine = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    playful_or_sophisticated = models.IntegerField(default=0,
                                                   validators=[MinValueValidator(-100), MaxValueValidator(100)])
    economical_or_luxurious = models.IntegerField(default=0,
                                                  validators=[MinValueValidator(-100), MaxValueValidator(100)])
    geometric_or_organic = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])
    abstract_or_literal = models.IntegerField(default=0, validators=[MinValueValidator(-100), MaxValueValidator(100)])

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.project_name}'


class ProjectFile(models.Model):
    project = models.ForeignKey(ProjectLogo, on_delete=models.CASCADE, null=True)
    project_file = models.ImageField(upload_to='projects/files/', null=True)
    title = models.CharField(max_length=100, null=True)
    file_description = models.TextField(max_length=500, null=True)
    status_options = (('Reference', 'Reference'), ('In progress', 'In progress'), ('Declined', 'Declined'),
                      ('Final', 'Final'))
    status = models.CharField(max_length=11, choices=status_options, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title}'


class CommentProjectFile(models.Model):
    project = models.ForeignKey(ProjectLogo, on_delete=models.CASCADE, null=True)
    project_file = models.ForeignKey(ProjectFile, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=300, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment}'


class ProjectActivity(models.Model):
    owner = models.ForeignKey(UserExtend, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(ProjectLogo, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f'{self.owner}'