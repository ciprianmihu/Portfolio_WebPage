# Generated by Django 4.1 on 2022-09-11 16:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0031_projectactivitymessage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentProjectFile',
            new_name='ProjectFileComment',
        ),
    ]