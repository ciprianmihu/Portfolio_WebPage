# Generated by Django 4.1 on 2022-09-02 06:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_projectlogo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlogo',
            name='style_attribute',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
