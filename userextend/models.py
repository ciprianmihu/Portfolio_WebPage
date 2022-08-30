from django.contrib.auth.models import User
from django.db import models


class UserExtend(User):
    gender_options = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    date_of_birth = models.DateField(null=True)
    email_confirmation = models.EmailField(max_length=100)
    gender = models.CharField(max_length=6, choices=gender_options)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(models.Model):
    user = models.OneToOneField(UserExtend, null=True, on_delete=models.CASCADE)

    profile_image = models.ImageField(default='CiprianM_Brand.png', upload_to='profiles/')
    company = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    
    def __str__(self):
        return f'{self.user.first_name}'
