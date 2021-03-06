# Generated by Django 4.0.2 on 2022-02-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_usercontact_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_time', models.TimeField(auto_now_add=True, verbose_name='Start Time')),
                ('e_time', models.TimeField(auto_now_add=True, verbose_name='End Time')),
                ('date', models.DateField(verbose_name='Date')),
                ('day', models.CharField(max_length=100, verbose_name='Day')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Set Available Time For Appointment',
                'verbose_name_plural': 'Set Available Time For Appointments',
            },
        ),
    ]
