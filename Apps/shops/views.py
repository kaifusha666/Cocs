from . import models

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
class ShopListView(LoginRequiredMixin, ListView):
    model = models.Shop
    template_name = 'shops_list.html'
    login_url = 'login'
class ShopDetailView(LoginRequiredMixin, DetailView):
    model = models.Shop
    template_name = 'shops_detail.html'
    login_url = 'login'
    def post(self, request, pk):
        models.PurchareUser.objects.create(product_id=models.Shop.objects.get(title=request.POST.get('title')), user_id=request.user)
        return HttpResponseRedirect(request.META.get('HTTP_ORIGIN') + f'/users/{request.user.pk}')
    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        context['PurchareUser'] = models.PurchareUser.objects.all()
        return context
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
