# Generated by Django 4.0.2 on 2022-02-22 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_statistic_active_case_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write a Heading')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Write a Description')),
                ('class_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write a Class Name for Styling')),
            ],
            options={
                'verbose_name': 'Choose Us',
                'verbose_name_plural': 'Choose Us',
            },
        ),
    ]
