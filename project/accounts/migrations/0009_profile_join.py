# Generated by Django 4.2.7 on 2023-12-20 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_profile_assess'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='join',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
