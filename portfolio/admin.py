from django.contrib import admin
from . models import (
    UserProfile,
    Statistic,
    Choose,
    Appointment,
    Testimonial,
    Blog,
    Contact,
    UserContact,
    Schedule
    )
# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_one', 'number_two', 'number_three', 'number_four')


@admin.register(Choose)
class ChooseAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'is_active')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading_one', 'heading_two', 'number', 'is_active')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quote', 'is_active')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'description', 'is_active')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'email', 'call', 'support', 'is_active')


@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('day', 's_time', 'e_time', 'date', 'is_active')