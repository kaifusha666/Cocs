from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(label = 'Адрес электронной почты')
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email',)



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

