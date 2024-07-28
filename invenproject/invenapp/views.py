# from django.shortcuts import render,redirect

# Create your views here.
# from .models import product
# from .forms import prodectForm
# def home(request):
#     return render(request,'invAPP/home.html')
# #create from
# def product_create_view(request):
#     form=prodectForm()
#     if request.method=='POST':
#         form=prodectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     return render(request,'invAPP/product_form.html', {'form':form})    
# def product_list_view(request):
#     products=product.objects.all()
#     return render(request,'invAPP/product_list.html',{'products':products})
# #update
# def product_update_view(request, product_id):
#     product=product.objects.get(product_id=product_id)
#     form=prodectForm(instance=product)
#     if request.method=='POST':
#         form=prodectForm(request.POST,instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     return render(request,'invAPP/product_form.html',{'form':form}) 
# #delete
# def product_delete_view(request,product_id):
#     product=product.objects.get(product_id=product_id)
#     if request.method=='POST':
#         product.delete()
#         return redirect('product_list')
#     return render(request,'invAPP/product_comfrim_delete.html',{'product':product})  

from django.shortcuts import render, redirect, get_object_or_404

# Import your models and forms
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'invAPP/home.html')

# Create form
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invAPP/product_form.html',{'form':form})

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invAPP/product_list.html', {'products':products})

# Update
def product_update_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invAPP/product_form.html', {'form': form})

# Delete
def product_delete_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invAPP/product_confirm_delete.html', {'product': product})
