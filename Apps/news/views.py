
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse


from . import models

class NewsListView(ListView):
    model = models.News
    template_name = 'news_list.html'
    login_url = 'login'
class NewsDetailView(DetailView):
    model = models.News
    template_name = 'news_detail.html'
    login_url = 'login'

    def post(self, request, pk):
        models.Comment.objects.create(news=models.News.objects.get(pk=pk),author=request.user, comment=request.POST.get('comment'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model =  models.News
    fields = ['title', 'body','image_news']
    template_name = 'news_edit.html'
    login_url = 'login'
class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = models.News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
    login_url = 'login'
class NewsCreateView(LoginRequiredMixin, CreateView):
    model = models.News
    template_name = 'news_new.html'
    fields = ['title', 'body', 'image_news']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SearchResultsView(ListView):
    model = models.News
    template_name = 'search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = models.News.objects.filter(
            Q(title__icontains=query)
        )
        return object_list