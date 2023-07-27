from django.db import models

class New(models.Model):
    heading = models.CharField(max_length=30,blank=True,null=True)
    new = models.CharField(max_length=30,blank=True,null=True)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.heading
        
