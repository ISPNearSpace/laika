from django.db import models


class Message(models.Model):
    imei = models.CharField(max_length=15)
    momsn = models.IntegerField()
    transmit_time = models.CharField(max_length=17) # Date & Time in UTC. ie:12-10-10 10:41:50
    iridium_latitude = models.FloatField()
    iridium_longitude = models.FloatField()
    iridium_cep = models.FloatField()
    data = models.CharField(max_length=150000)
