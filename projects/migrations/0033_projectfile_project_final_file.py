# Generated by Django 4.1 on 2022-09-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_rename_commentprojectfile_projectfilecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfile',
            name='project_final_file',
            field=models.FileField(blank=True, null=True, upload_to='projects/finalfiles/'),
        ),
    ]
