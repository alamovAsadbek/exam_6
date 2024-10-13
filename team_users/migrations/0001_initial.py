# Generated by Django 5.1.2 on 2024-10-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('first_name_en', models.CharField(max_length=50, null=True, verbose_name='First Name')),
                ('first_name_uz', models.CharField(max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('last_name_en', models.CharField(max_length=50, null=True, verbose_name='Last Name')),
                ('last_name_uz', models.CharField(max_length=50, null=True, verbose_name='Last Name')),
                ('image', models.ImageField(upload_to='team_users/images/', verbose_name='Image')),
                ('role', models.CharField(max_length=100, verbose_name='Role')),
                ('role_en', models.CharField(max_length=100, null=True, verbose_name='Role')),
                ('role_uz', models.CharField(max_length=100, null=True, verbose_name='Role')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_en', models.TextField(null=True, verbose_name='Description')),
                ('description_uz', models.TextField(null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Team User',
                'verbose_name_plural': 'Team Users',
            },
        ),
    ]
