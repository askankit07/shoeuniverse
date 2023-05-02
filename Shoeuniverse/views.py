from django.shortcuts import render,redirect
from .models import CreateNewAccount
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenApi,WomenApi,KidsApi,NewArrivalApi
from .serializer import MenApiSerializer,WomenApiSerializer,KidsApiSerializer,NewArrivalSerializer

import requests

class MenView(APIView):

    def get(self,request,*args,**kwargs):
        result=MenApi.objects.all()
        serializer=MenApiSerializer(result,many=True)
        return Response({'status':'success','MenApi':serializer.data},status=200)
    def post(self,request):
        serializer=MenApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else: 
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class WomenView(APIView):
    def get(self,request,*args,**kwargs):
        result=WomenApi.objects.all()
        serializer=WomenApiSerializer(result,many=True)
        return Response({'status':'success','WomenApi':serializer.data},status=200)
    def post(self,request):
        serializer=WomenApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else: 
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class KidsView(APIView):
    def get(self,request,*args,**kwargs):
        result=KidsApi.objects.all()
        serializer=KidsApiSerializer(result,many=True)
        return Response({'status':'success','KidsApi':serializer.data},status=200)
    def post(self,request):
        serializer=KidsApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else: 
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class NewArrivalView(APIView):
    def get(self,request,*args,**kwargs):
        result=NewArrivalApi.objects.all()
        serializer=NewArrivalSerializer(result,many=True)
        return Response({'status':'success','NewarrivalApi':serializer.data},status=200)
    def post(self,request):
        serializer=NewArrivalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else: 
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

def index(request):
    if 'user' in request.session:
        current_user=request.session['user']
        param={'current_user':current_user}
        return render(request,'index.html',param)
    return render(request,'index.html')

def signUp(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        if CreateNewAccount.objects.filter(email=email).count()>0:
            error='Already sign up'
            return render(request,'signup.html',{'error':error})
        else:
            info=CreateNewAccount(first_name=fname,last_name=lname,email=email,password=pwd)
            info.save()
            return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        check_user=CreateNewAccount.objects.filter(email=email,password=password)
        if check_user:
            userData=CreateNewAccount.objects.get(email=email)
            first_name=userData.first_name
            request.session['user']=first_name
            return redirect('index')
        else:
            error='Invalid email or password'
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('index')

def men(request):
    response=requests.get('http://127.0.0.1:8000/menapi/')
    data=response.json()
    return render(request,'men.html',{'data':data['MenApi']})

def women(request):
    response=requests.get('http://127.0.0.1:8000/womenapi/')
    data=response.json()
    return render(request,'women.html',{'data':data['WomenApi']})
    
def kids(request):
    response=requests.get('http://127.0.0.1:8000/kidsapi/')
    data=response.json()
    return render(request,'kids.html',{'data':data['KidsApi']})

def newArrivals(request):
    response=requests.get('http://127.0.0.1:8000/newarrivalsapi/')
    data=response.json()
    return render(request,'new-arrivals.html',{'data':data['NewarrivalApi']})
