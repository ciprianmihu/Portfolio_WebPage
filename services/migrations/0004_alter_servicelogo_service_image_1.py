# Generated by Django 4.1 on 2022-09-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_servicelogo_price_alter_servicelogo_turnaround'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelogo',
            name='service_image_1',
            field=models.ImageField(null=True, upload_to='services/'),
        ),
    ]
