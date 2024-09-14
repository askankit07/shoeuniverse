from django.shortcuts import render,redirect
import requests
from .models import *
from shoeApi.models import *

def index(request):
    if 'user' in request.session:
        current_user=request.session['user']
        return render(request,'index.html',{'current_user':current_user})
    return render(request,'index.html')

def login(request):
    if 'user' in request.session:
        return redirect('index')
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        check_user=Customer.objects.filter(email=email,password=password)
        if check_user:
            userData=Customer.objects.get(email=email)
            first_name=userData.first_name
            email=userData.email
            request.session['user']=first_name
            request.session['email']=email
            return redirect('index')
        else:
            error='Invalid email or password'
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')

def signUp(request):
    if 'user' in request.session:
        return redirect('index')

    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        if Customer.objects.filter(email=email).count()>0:
            error='This email already used'
            return render(request,'signup.html',{'error':error})
        else:
            info=Customer(first_name=fname,last_name=lname,email=email,password=pwd)
            info.save()
            return redirect('login')

    return render(request,'signup.html')
    
def logout(request):
    try:
        del request.session['user']
        del request.session['email']
    except:
        return redirect('login')
    return redirect('index')

def men(request):
  
    if 'user' in request.session:
        current_user=request.session['user']
        response=requests.get('http://64.227.188.237/api/men/')
        data=response.json()
        return render(request,'men.html',{'data':data,'current_user':current_user})
    else:
        response=requests.get('http://64.227.188.237/api/men/')
        data=response.json()
        return render(request,'men.html',{'data':data})

def women(request):
    if 'user' in request.session:
        current_user=request.session['user']
        response=requests.get('http://64.227.188.237/api/women/')
        data=response.json()
        return render(request,'women.html',{'data':data,'current_user':current_user})
    else:
        response=requests.get('http://64.227.188.237/api/women/')
        data=response.json()
        return render(request,'women.html',{'data':data})

def kids(request):
    if 'user' in request.session:
        current_user=request.session['user']
        response=requests.get('http://64.227.188.237/api/kids/')
        data=response.json()
        return render(request,'kids.html',{'data':data,'current_user':current_user})
    else:
        response=requests.get('http://64.227.188.237/api/kids/')
        data=response.json()
        return render(request,'kids.html',{'data':data})

def newArrivals(request):
    if 'user' in request.session:
        current_user=request.session['user']
        response=requests.get('http://64.227.188.237/api/newArrivals/')
        data=response.json()
        return render(request,'new-arrivals.html',{'data':data,'current_user':current_user})
    else:
        response=requests.get('http://64.227.188.237/api/newArrivals/')
        data=response.json()
        return render(request,'new-arrivals.html',{'data':data})

def orderSummary(request,id,url):
    
    if 'user' in request.session:
        current_user=request.session['user']
        email=request.session['email']
        ForeignKey=Customer.objects.get(email=email)
        if request.method=='POST':
            id=request.POST.get('id')
            name=request.POST.get('name')
            qty=request.POST.get('quantity')
            amount=request.POST.get('amount')
            imageUrl=request.POST.get('imageUrl')
            qty=int(qty)
            amount=int(amount)

            order=Order(productId=id,productName=name,productQty=qty,totalAmount=(amount*qty),imageUrl=imageUrl,foreignKey=ForeignKey)
            order.save()
            return redirect('index')
        response=requests.get('http://64.227.188.237/api/'+url+'/'+id)
        product=response.json()
        return render(request,'orderSummary.html',{'product':product,'current_user':current_user})
    return redirect('index')
    

def search(request):
    if request.method=='POST':
        if 'user' in request.session:
            current_user=request.session['user']
        else:
            current_user=''
        s=request.POST.get('search-bar')
        s=s.title()
        kids=KidsModel.objects.filter(name=s)
        women=WomenModel.objects.filter(name=s)
        men=MenModel.objects.filter(name=s)
        if kids:
            return render(request,'search.html',{'shoeinfo':kids,'url':'kids','current_user':current_user})
        if women:
            return render(request,'search.html',{'shoeinfo':women,'url':'women','current_user':current_user})
        if men:
            return render(request,'search.html',{'shoeinfo':men,'url':'men','current_user':current_user})
        else:
            return render(request,'search.html',{'NoData':s,'current_user':current_user})
    
    return redirect('index')

def importOrders(request):
    if 'user' in request.session:
        current_user=request.session['user']
        email=request.session['email']
    
        ForeignKey=Customer.objects.get(email=email)
        data=Order.objects.filter(foreignKey=ForeignKey)

        return render(request,'confirmOrder.html',{'current_user':current_user,'data':data})
    
    return redirect('index')

def cancelOrder(request, id):
    delOrder=Order.objects.get(orderId=id)
    delOrder.delete()
    return redirect('orders')

def addToCart(request,id):
    if 'user' in request.session:
        email=request.session['email']
        ForeignKey=Customer.objects.get(email=email)

        kids=KidsModel.objects.filter(id=id)
        women=WomenModel.objects.filter(id=id)
        men=MenModel.objects.filter(id=id)
        newArrivals=NewArrivalModel.objects.filter(id=id)
        if kids:
            for i in kids:
                cart=Cart(productId=i.id,productName=i.name,Amount=i.price,description=i.description,imageUrl=i.imageUrl,foreignKey=ForeignKey)
                cart.save()
            return redirect('kids')
        if women:
            for i in women:
                cart=Cart(productId=i.id,productName=i.name,Amount=i.price,description=i.description,imageUrl=i.imageUrl,foreignKey=ForeignKey)
                cart.save()
            return redirect('women')
        if men:
            for i in men:
                cart=Cart(productId=i.id,productName=i.name,Amount=i.price,description=i.description,imageUrl=i.imageUrl,foreignKey=ForeignKey)
                cart.save()
            return redirect('men')
        if newArrivals:
            for i in newArrivals:
                cart=Cart(productId=i.id,productName=i.name,Amount=i.price,description=i.description,imageUrl=i.imageUrl,foreignKey=ForeignKey)
                cart.save()
            return redirect('newArrivals')
    
    return redirect('index')

def cart(request):
    if 'user' in request.session:
        current_user=request.session['user']
    else:
        current_user=''
    return render(request,'cart.html',{'current_user':current_user})

def importCart(request):
    if 'user' in request.session:
        current_user=request.session['user']
        email=request.session['email']
    
        ForeignKey=Customer.objects.get(email=email)
        data=Cart.objects.filter(foreignKey=ForeignKey)
        return render(request,'cart.html',{'current_user':current_user,'data':data})
    
    return render(request,'cart.html')

def removeCart(request, id):
    delcart=Cart.objects.get(CartId=id)
    delcart.delete()
    return redirect('cart')