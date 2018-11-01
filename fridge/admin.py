from django.contrib import admin
from .models import Grocery,Cart,Profile
# Register your models here.

admin.site.register(Grocery)
admin.site.register(Cart)
admin.site.register(Profile)