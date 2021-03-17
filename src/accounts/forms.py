from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class MyAuthenticationForm(AuthenticationForm):
    """ Authentication Form """
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Password'}),
    )
