from . import models

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ShopListView(LoginRequiredMixin, ListView):
    model = models.Shop
    template_name = 'shops_list.html'
    login_url = 'login'
class ShopDetailView(LoginRequiredMixin, DetailView):
    model = models.Shop
    template_name = 'shops_detail.html'
    login_url = 'login'
class ShopUpdateView(LoginRequiredMixin, UpdateView):
    model =  models.Shop
    fields = ['title', 'price','image_shop']
    template_name = 'shops_edit.html'
    login_url = 'login'
class ShopDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Shop
    template_name = 'shops_delete.html'
    success_url = reverse_lazy('shop_list')
    login_url = 'login'
class ShopCreateView(LoginRequiredMixin, CreateView):
    model = models.Shop
    template_name = 'shops_new.html'
    fields = ['title', 'price','image_shop']
    login_url = 'login'