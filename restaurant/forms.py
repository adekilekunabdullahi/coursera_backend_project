from django import forms
from .models import Booking
from django.contrib.auth.models import User


# Code added for loading form data on the Booking page
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class UserForms(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=200)