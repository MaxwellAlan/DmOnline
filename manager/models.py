from django.contrib.auth.models import User
from django.db import models
import json

# Create your models here.
class MapPoi(models.Model):
    row_num=models.IntegerField(blank=False)
    name_id=models.IntegerField(blank=False)
    address=models.CharField(max_length=400,blank=True)
    longitude=models.FloatField(blank=False)
    latitude=models.FloatField(blank=False)
    precise=models.BooleanField()
    level=models.CharField(max_length=100)
    food=models.IntegerField(blank=False)
    hotel=models.IntegerField(blank=False)
    shopping=models.IntegerField(blank=False)
    dailyservice=models.IntegerField(blank=False)
    entertainment=models.IntegerField(blank=False)
    education=models.IntegerField(blank=False)
    medical=models.IntegerField(blank=False)
    financial=models.IntegerField(blank=False)
    traffic=models.IntegerField(blank=False)

    def __str__(self):
        return "name id is:{0},longitude:{1},latitude:{2}".format(self.name_id,self.longitude,self.latitude)

    def to_json(self):
        return {"id":self.id,"longitude":self.longitude,"latitude":self.latitude}