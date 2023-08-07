from django.shortcuts import render
from .models import New
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import *

def new(request):
    if(request.method=="POST"):
        heading = request.POST.get('heading')
        new = request.POST.get('new')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        point = GEOSGeometry("POINT("+lat+" "+lng+")", srid=4326)

        new = New(heading=heading, new= new, lat=lat, lon=lng, point=point)
        new.save()

        
        pnt = GEOSGeometry("POINT("+lat+" "+lng+")", srid=4326)
        some = New.objects.filter(point__distance_lte=(pnt,D(km=7)))
        return render(request,'leaf.html',{'new':some})


    
    new = New.objects.all()
    return render(request,'leaf.html',{'new': new})

def markers(request):
    new = New.objects.all()
    return render(request,'leaf.html',{'new': new})
