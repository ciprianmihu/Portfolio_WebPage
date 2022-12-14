# Generated by Django 4.1 on 2022-09-04 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userextend', '0007_alter_userprofile_profile_image'),
        ('projects', '0013_rename_style_attribute_projectlogo_classic_or_modern_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file_description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userextend.userextend')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectlogo')),
            ],
        ),
    ]
