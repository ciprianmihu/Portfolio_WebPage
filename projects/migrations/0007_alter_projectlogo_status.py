# Generated by Django 4.1 on 2022-08-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_projectlogo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlogo',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Invited', 'Invited'), ('Started', 'Started'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Draft', max_length=9, null=True),
        ),
    ]
