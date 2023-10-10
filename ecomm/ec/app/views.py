from django.shortcuts import render, redirect
from django.views import View
from . models import Product, Customer
from app.forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
# Create your views here.
def base_view(request,*args,**Kwargs):
    return render(request,"app/base.html",{})


def home_view(request,*args,**Kwargs):
    return render(request,"app/home.html",{})

class CategoryView(View):
    def get(self, request, val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/product_detail.html", locals())


def about_view(request,*args,**Kwargs):
    return render(request,"app/about.html",{})


'''def contact_view(request,*args,**Kwargs):
    return render(request,"app/contact.html",{})'''

class CategoryView(View):
    def get(self, request, val):
        product=Product.objects.filter(title=val)
        #recuperer le title des produits de chaque valeur de category 
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, "app/registration.html", locals())

    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registered Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "app/registration.html", locals())



class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm
        return render(request, "app/profile.html", locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name = name,locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Address Updated Successfully")
        else:
             messages.warning(request, "Invalid Input Data")
        return render(request, "app/profile.html", locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,"app/address.html", locals())

class UpdateAddress(View):
    def get(self,request, pk):
        pk = Customer.objects.filter(user=request.user).values('id')
        form = CustomerProfileForm
        return render(request, "app/update.htm", locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        add = Customer.objects.get(pk=pk)
        if form.is_valid():
            add.user = request.user
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Address Updated Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")


