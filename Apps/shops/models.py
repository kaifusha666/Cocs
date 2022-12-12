from django.db import models
from django.urls import reverse

class Shop(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image_shop = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop_detail', args=[str(self.id)])