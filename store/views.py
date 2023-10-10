from django.shortcuts import render

# Create your views here.
def store_view(request,*args,**kwargs):
    return render(request,"store/store.html",{})

def checkout_view(request,*args,**kwargs):
    return render(request,"store/checkout.html",{})

def cart_view(request,*args,**kwargs):
    return render(request,"store/cart.html",{})