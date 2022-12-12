from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from . import models
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Profiles(LoginRequiredMixin, TemplateView):
    model = models.Profile
    template_name = 'profile.html'
    login_url = 'login'
