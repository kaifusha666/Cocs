from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from . import models
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.apps import apps

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Profiles(LoginRequiredMixin, ListView):
    model = apps.get_model('shops', 'PurchareUser')
    template_name = 'profile.html'
    login_url = 'login'