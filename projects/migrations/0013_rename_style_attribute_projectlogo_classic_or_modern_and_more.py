# Generated by Django 4.1 on 2022-09-02 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_projectlogo_client_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectlogo',
            old_name='style_attribute',
            new_name='classic_or_modern',
        ),
        migrations.AddField(
            model_name='projectlogo',
            name='abstract_or_literal',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='projectlogo',
            name='economical_or_luxurious',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='projectlogo',
            name='feminine_or_masculine',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='projectlogo',
            name='geometric_or_organic',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='projectlogo',
            name='mature_or_youthful',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='projectlogo',
            name='playful_or_sophisticated',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='projectlogo',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Started', 'Started'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=9, null=True),
        ),
    ]