# Generated by Django 4.1 on 2022-09-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_projectfile_created_at_projectfile_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfile',
            name='project_file',
            field=models.ImageField(null=True, upload_to='projects/files/'),
        ),
    ]
