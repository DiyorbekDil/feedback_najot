# Generated by Django 5.1.1 on 2024-10-12 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_commentmodel_content_and_more'),
        ('offers_problems', '0003_alter_offermodel_created_at_and_more'),
        ('users', '0006_remove_usermodel_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
