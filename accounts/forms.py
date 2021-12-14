from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER = [
        (MALE, "Male"),
        (FEMALE, "Female"),
    ]
    gender = forms.TypedChoiceField(
        choices=GENDER,
        initial=MALE,
        coerce=str,
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'username', 'password1', 'password2', 'gender']
