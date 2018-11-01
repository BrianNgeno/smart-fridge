from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Grocery,Cart
from .forms import ProfileForm,CartForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.



@csrf_exempt
def home(request):
    items = Grocery.objects.all()
    Cartform = CartForm()
    return render(request,'home.html',locals())

def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/edit_profile.html', locals())

def add_to_cart(request,id):
    if request.method == 'POST':
        grocery = Grocery.objects.get(id=id)
        Cartform = CartForm(request.POST)
        if Cartform.is_valid():
            form = Cartform.save(commit=False)
            form.user = request.user
            form.item = grocery
            form.save()
        return redirect ('cart')

def delete_cart(request,id):
    item = Cart.objects.get(id=id)
    Cart.delete_item(item)
    return redirect('cart')

def empty(request):
    item = Cart.objects.filter(user=request.user).delete()
    return redirect('cart',locals())



def cart(request):
    items = Cart.objects.filter(paid='False')
    prices = []
    for item in items:
       price = int(item.item.price)
       prices.append(price)
    print(prices)
    total = sum(prices)
    return render(request,'cart.html',locals())