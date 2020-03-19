from django.db import models

# Create your models here.

class Data(models.Model):
    imei_code = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    battery = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return "{} {} {} {}".format(self.imei_code,
                                 self.longitude, 
                                 self.latitude,
                                 self.battery)


class MobileData(models.Model):
    imei_code = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    battery = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return "{} {} {} {}".format(self.imei_code,
                                 self.longitude, 
                                 self.latitude,
                                 self.battery)