# Generated by Django 4.1 on 2022-09-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_remove_projectfile_project_final_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfile',
            name='project_final_file',
            field=models.FileField(blank=True, null=True, upload_to='projects/finalfiles/'),
        ),
        migrations.AlterField(
            model_name='projectfile',
            name='project_file',
            field=models.ImageField(null=True, upload_to='projects/files/'),
        ),
    ]