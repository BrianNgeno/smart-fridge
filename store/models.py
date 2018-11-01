from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length = 50 )
    thumbnail = models.ImageField(upload_to='product/vegetables' , default='')
    price = models.PositiveIntegerField()


