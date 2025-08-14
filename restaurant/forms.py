from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'date': 'Booking Date',
            'time': 'Booking Time',
            'guests': 'Number of Guests',
            'message': 'Special Requests '
            '(optional)',
            
        }
