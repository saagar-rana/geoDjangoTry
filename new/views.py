from django.shortcuts import render
from .models import New

def new(request):
    if(request.method=="POST"):
        heading = request.POST.get('heading')
        new = request.POST.get('new')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        new = New(heading=heading, new= new, lat=lat, lon=lng)
        new.save()
        
        new = New.objects.all()
        return render(request,'leaf.html',{'new': new})


    
    new = New.objects.all()
    return render(request,'leaf.html',{'new': new})

def markers(request):
    new = New.objects.all()
    return render(request,'leaf.html',{'new': new})
