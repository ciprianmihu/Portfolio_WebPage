# Generated by Django 4.1 on 2022-08-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_name', models.CharField(max_length=50)),
                ('logo_description', models.TextField(max_length=500)),
                ('company_name', models.CharField(max_length=50)),
                ('company_description', models.TextField(max_length=500)),
                ('company_industry', models.CharField(max_length=50)),
                ('logo_image_1', models.ImageField(null=True, upload_to='portfoliologo/')),
                ('logo_image_2', models.ImageField(blank=True, null=True, upload_to='portfoliologo/')),
                ('logo_image_3', models.ImageField(blank=True, null=True, upload_to='portfoliologo/')),
                ('logo_image_4', models.ImageField(blank=True, null=True, upload_to='portfoliologo/')),
                ('logo_image_5', models.ImageField(blank=True, null=True, upload_to='portfoliologo/')),
                ('logo_image_6', models.ImageField(blank=True, null=True, upload_to='portfoliologo/')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
