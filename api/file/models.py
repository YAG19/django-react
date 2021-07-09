from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=20 ,default='')
    file = models.FileField(max_length=None, upload_to='file/', blank=False)
