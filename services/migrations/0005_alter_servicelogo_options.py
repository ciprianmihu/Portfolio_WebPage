# Generated by Django 4.1 on 2022-09-29 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_servicelogo_service_image_1'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicelogo',
            options={'ordering': ['id']},
        ),
    ]
