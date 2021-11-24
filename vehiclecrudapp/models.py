from django.db import models
import os
import datetime
# Create your models here.
def filepath(request,filename):
    old_filename=filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow,old_filename)
    return os.path.join('uploads/',filename)

class vehicle(models.Model):
    regno = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    speed = models.CharField(max_length=122,null=True)
    avgspeed = models.CharField(max_length=122)
    temp = models.CharField(max_length=122)
    fuel = models.CharField(max_length=122)
    engine = models.CharField(max_length=122)
    location = models.CharField(max_length=122)
    image = models.ImageField(upload_to=filepath, null=True,blank=True)