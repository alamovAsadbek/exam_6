# Generated by Django 5.1.1 on 2024-10-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_usermodel_image_alter_usermodel_linkedin_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
    ]
