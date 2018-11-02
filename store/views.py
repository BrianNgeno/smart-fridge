from django.shortcuts import render
from django.http import HttpResponse
from fridge.models import Cart

# Create your views here.
def home_page(request):
    return render(request,'home.html')

def order(request):
    items = Cart.objects.filter(paid='False')
    prices = []
    for item in items:
       price = int(item.item.price)
       prices.append(price)
    print(prices)
    total = sum(prices)
    return render(request,'order.html',locals())