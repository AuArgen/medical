from django.contrib import admin

from patient.models import Patient, QueuePatient


# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone',)

@admin.register(QueuePatient)
class QueuePatientAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient',)
