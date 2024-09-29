from django.shortcuts import render,redirect
from .models import shoe


def index(request):
    return render(request,'index.html')


def add(request):
    if request.method=='POST':
        tb=shoe()
        tb.name=request.POST.get('name')
        tb.cat=request.POST.get('cat')
        tb.size=request.POST.get('size')
        tb.color=request.POST.get('color')
        tb.price=request.POST.get('price')
        tb.image=request.FILES.get('prod_image')
        tb.save()
        return redirect('/')
    return render(request,'add.html')


def show(request):
    dt=shoe.objects.all()
    return render(request,'show.html',{'x':dt})

def edit(request,a):
    dt=shoe.objects.get(id=a)
    if request.method=='POST':
        dt.name=request.POST.get('name')
        dt.cat=request.POST.get('cat')
        dt.size=request.POST.get('size')
        dt.color=request.POST.get('color')
        dt.price=request.POST.get('price')
        dt.save()
        return redirect('/show/')

    return render(request,'edit.html',{'x':dt})

def dlt(request,a):
    dt=shoe.objects.get(id=a)
    dt.delete()
    return redirect('/show/')