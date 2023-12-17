from django import forms
from .models import User
from django.contrib.auth.models import Group


# Need To Work More
class GroupAdminForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_staff=True, is_active=True))

    class Meta:
        model = Group
        fields = '__all__'


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)

    class Meta:
        model = User
        fields = ('email', 'password',)

