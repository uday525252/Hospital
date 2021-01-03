from django.contrib import admin
from testapp.models import Doctor,Patient,Appointment

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display=['doctor_name','mobile_no','shift','specialization','experience']


class PatientAdmin(admin.ModelAdmin):
    list_display=['patient_name','age','mobile_no','disease','blood_group','address']


class AppointmentAdmin(admin.ModelAdmin):
    list_display=['doctor','patient','date_and_time']


admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Appointment,AppointmentAdmin)
