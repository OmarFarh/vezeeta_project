# Generated by Django 4.2.7 on 2023-12-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_create_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='create_post',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
