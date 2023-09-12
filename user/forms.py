from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationForm(forms.ModelForm):
    pw = forms.CharField(label='Password', widget=forms.PasswordInput)
    pw2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('uid', )

    def clean_password2(self):
        pw = self.cleaned_data.get("pw")
        pw2 = self.cleaned_data.get("pw2")
        if pw and pw2 and pw != pw2:
            raise forms.ValidationError("Passwords don't match")
        return pw2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["pw"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('uid', 'pw')

    def clean_password(self):
        return self.initial["password"]