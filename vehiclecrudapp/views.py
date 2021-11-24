from django.shortcuts import render, HttpResponse
from vehiclecrudapp.models import vehicle
import os
# Create your views here.
def index(request):
    return render(request,'index.html')

def update(request,id):
    vs = vehicle.objects.filter(regno=str(id))
    if request.method == "POST":
        vs.update(regno=request.POST.get('regno'),
                state = request.POST.get('state'),
                speed = request.POST.get('speed'),
                avgspeed = request.POST.get('avgspeed'),
                temp = request.POST.get('temp'),
                fuel = request.POST.get('fuel'),
                engine = request.POST.get('engine'),
                location = request.POST.get('location'))
        return list(request)
    context = {'vehicles':vs[0]}
    return render(request,'update.html',context)


def add(request):
    return render(request,'add.html')
def details(request):
    if request.method == "POST":
        Regno = request.POST.get('regno')
        State = request.POST.get('state')
        Speed = request.POST.get('speed')
        Avgspeed = request.POST.get('avgspeed')
        Temp = request.POST.get('temp')
        Fuel = request.POST.get('fuel')
        Engine = request.POST.get('engine')
        Location = request.POST.get('location')
        Vehicle = vehicle(regno=Regno, state = State,speed = Speed, avgspeed = Avgspeed, temp = Temp, fuel = Fuel, engine = Engine, location=Location)
        if len(request.FILES) !=0:
            Vehicle.image = request.FILES['image']
        Vehicle.save()
        context = {'vehicles': Vehicle}
        return render(request,'details.html',context)

    return render(request,'details.html')

def list(request):
    v = vehicle.objects.all()
    context= {'vehicles':v}
    return render(request,'list.html',context)

def getdetails(request,id):
    vs = vehicle.objects.all().filter(regno=str(id))
    context = {'vehicles':vs[0]}
    return render(request,'details.html',context)