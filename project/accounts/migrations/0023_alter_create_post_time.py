# Generated by Django 4.2.7 on 2023-12-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_create_post_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_post',
            name='time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
