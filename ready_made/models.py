from django.db import models


class ReadyLogo(models.Model):
    logo_name = models.CharField(max_length=50)
    logo_description = models.TextField(max_length=1000)
    company_description = models.TextField(max_length=1000, blank=True)
    company_industry = models.CharField(max_length=50, blank=True)
    logo_image_1 = models.ImageField(upload_to='readylogo/', null=True)
    optional_logo_image_2 = models.ImageField(upload_to='readylogo/', null=True, blank=True)
    optional_logo_image_3 = models.ImageField(upload_to='readylogo/', null=True, blank=True)
    optional_logo_image_4 = models.ImageField(upload_to='readylogo/', null=True, blank=True)
    optional_logo_image_5 = models.ImageField(upload_to='readylogo/', null=True, blank=True)
    optional_logo_image_6 = models.ImageField(upload_to='readylogo/', null=True, blank=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.logo_name}'
