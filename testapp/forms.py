from django import forms
from testapp.models import Doctor,Patient


class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"

        widgets={
        'doctor_name':forms.TextInput(attrs={'class':'form-control'}),
        'mobile_no':forms.TextInput(attrs={'class':'form-control'}),
        'shift':forms.Select(attrs={'class':'form-control'}),
        'specialization':forms.TextInput(attrs={'class':'form-control'}),
        'experience':forms.TextInput(attrs={'class':'form-control'})
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"

        widgets={
        'patient_name':forms.TextInput(attrs={'class':'form-control'}),
        'age':forms.TextInput(attrs={'class':'form-control'}),
        'mobile_no':forms.TextInput(attrs={'class':'form-control'}),
        'disease':forms.TextInput(attrs={'class':'form-control'}),
        'blood_group':forms.TextInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'})
        }
