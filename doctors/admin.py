from django.contrib import admin

from doctors.models import Directions, Doctor, Testimony


# Register your models here.
@admin.register(Directions)
class DirectionsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)
    search_fields = ('name',)


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('doctor',)
