from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

Customer = get_user_model()

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'password1', 'password2')

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'phone_number', 'address']