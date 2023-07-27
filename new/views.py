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

        return render(request,'leaf.html')


    return render(request,'leaf.html')
