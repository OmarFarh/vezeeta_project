# Generated by Django 4.2.7 on 2023-12-20 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_profile_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
