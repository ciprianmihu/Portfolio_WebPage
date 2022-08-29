from django.db import models


class ServiceLogo(models.Model):
    service_name = models.CharField(max_length=50)
    service_description = models.TextField(max_length=3000)
    service_deliverable = models.TextField(max_length=3000)
    turnaround = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    service_image_1 = models.ImageField(upload_to='services/', null=True, blank=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.service_name}'
