from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopListView.as_view(), name='shop_list'),
    path('<int:pk>/edit/', views.ShopUpdateView.as_view(), name='shop_edit'),
    path('<int:pk>/', views.ShopDetailView.as_view(), name='shop_detail'),
    path('<int:pk>/delete/', views.ShopDeleteView.as_view(), name='shop_delete'),
    path('new/', views.ShopCreateView.as_view(), name='shop_new'),
]