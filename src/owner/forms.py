from django import forms
from .models import Salon
from .models import Appointment

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ['name', 'image', 'location', 'opening_hours', 'contact_no', 'services','facilities']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'location': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'opening_hours': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'contact_no': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'services': forms.Textarea(
                attrs={'class': 'form-control'}
                ),
            'facilities':forms.Textarea(
                attrs={'class': 'form-control'}
                ),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['image','salon','contact_no' ,'date', 'time', 'service']
        widgets = {
            'contact_no': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
                ),
            'time': forms.TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}
                ),
            'service': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
        }