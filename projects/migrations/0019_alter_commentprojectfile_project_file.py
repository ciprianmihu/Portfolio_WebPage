# Generated by Django 4.1 on 2022-09-08 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_projectfile_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentprojectfile',
            name='project_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectfile'),
        ),
    ]