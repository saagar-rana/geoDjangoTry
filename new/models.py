from django.db import models
from django.contrib.gis.db import models

class New(models.Model):
    heading = models.CharField(max_length=30,blank=True,null=True)
    new = models.CharField(max_length=30,blank=True,null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    point = models.PointField(srid=4326,blank=True, null=True)

    def __str__(self):
        return self.heading
