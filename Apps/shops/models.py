from django.db import models
from django.urls import reverse
from django.conf import settings
class Shop(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image_shop = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop_detail', args=[str(self.id)])

class PurchareUser(models.Model):
    product_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id

    def get_absolute_url(self):
        return reverse('shop', args=[str(self.product_id)])
