# Generated by Django 4.1 on 2022-08-28 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userextend', '0002_userextend_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(default='CiprianM_Brand.png', upload_to='profiles/')),
                ('bio', models.TextField(blank=True, max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userextend.userextend')),
            ],
        ),
    ]
