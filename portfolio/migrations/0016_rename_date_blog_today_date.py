# Generated by Django 4.0.2 on 2022-02-22 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_blog_image_two'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='today_date',
        ),
    ]
