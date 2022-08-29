# Generated by Django 4.1 on 2022-08-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_projectlogo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlogo',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Started', 'Started'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='draft', max_length=9, null=True),
        ),
    ]
