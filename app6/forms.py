from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fName', 'lName', 'Aadhaar', 'Pincode']

class SavingsAccountForm(forms.Form):
    initial_amount = forms.DecimalField(max_digits=10, decimal_places=2)
