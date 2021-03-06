from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Şifre", widget=PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label="Kullanıcı adı")
    password = forms.CharField(
        max_length=20, label="Password", widget=forms.PasswordInput)
    confirm = forms.CharField(
        max_length=20, label="Confirm Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {
            "username": username,
            "password": password

        }
