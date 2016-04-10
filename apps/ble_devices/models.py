from django.db import models
from django.utils import timezone


class BLEDevice(models.Model):
    name = models.CharField(max_length=256)
    ble_device_id = models.CharField(max_length=256)
    registered_on = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return str(self.name)


class BLEData(models.Model):
	device = models.ForeignKey(BLEDevice, related_name="data")
	temperature = models.FloatField()
	battery_level = models.FloatField()
	humidity= models.FloatField()
	added_on = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
	    return str(self.device.name)