# Generated by Django 5.1.1 on 2024-10-10 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
