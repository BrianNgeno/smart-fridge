from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import datetime as dt


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


        
class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    Bio = models.TextField(max_length = 50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    grocery = models.ForeignKey('Grocery',related_name='grocery',null=True)

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
    
    @classmethod
    def search_user(cls, name):
        userprof = Profile.objects.filter(user__username__icontains = name)
        return userprof


# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length = 50 )
    image = models.ImageField(upload_to='product/vegetables' , default='')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    price = models.CharField(max_length = 50 )

# class Order(models.Model):
#     name = models.CharField(max_length = 50 )
#     price = models.CharField(max_length = 50 )
#     is_ordered = models.BooleanField(default=False)
#     order_date = models.DateTimeField(auto_now_add=True, null=True)

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart')
    item = models.ForeignKey(Grocery,related_name='cart')
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    paid = models.CharField(default='False',max_length=20)
    
    def __str__(self):
        return self.paid

    class Meta:
        ordering = ['-id']

    def save_item(self):
        self.save()

    def delete_item(self):
        self.delete()

