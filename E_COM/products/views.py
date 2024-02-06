from django.shortcuts import render
from .models import product
from django.contrib.auth.models import User

# Create your views here.
def product_index(request):
    
    productData=product.objects.all()#.order_by('sevice_icon')[:3]
    
    if request.method=='GET':
        st=request.GET.get('productname')
        if st != None:
            productData=product.objects.filter(product_icon__icontains=st)
    return render(request, "product_index.html",{'productData':productData})


def product_profile(request,st):
    
    productData=product.objects.all()#.order_by('sevice_icon')[:3]

    productData=product.objects.filter(product_icon__icontains=st)
    
    return render(request, "product_profile.html",{'productData':productData})

def product_buy(request,st):
    return render(request, "product_buy.html",{'productname':st})