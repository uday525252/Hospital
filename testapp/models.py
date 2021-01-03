from django.db import models

from django.urls import reverse

# Create your models here.
class Doctor(models.Model):
    doctor_name=models.CharField(max_length=150)
    mobile_no=models.IntegerField()
    shift_choices=(
    ('day shift','Day Shift'),
    ('night shift','Night Shift')
    )
    shift=models.CharField(max_length=30,choices=shift_choices)
    specialization=models.CharField(max_length=100)
    experience=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("doc_detail")


    def __str__(self):
        return self.doctor_name

class Patient(models.Model):
    patient_name=models.CharField(max_length=40)
    age=models.IntegerField()
    mobile_no=models.IntegerField()
    disease=models.CharField(max_length=100)
    blood_group=models.CharField(max_length=40)
    address=models.TextField()

    def get_absolute_url(self):
        return reverse("pat_detail")

    def __str__(self):
        return self.patient_name


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.OneToOneField(Patient,on_delete=models.CASCADE)
    date_and_time=models.DateTimeField()
