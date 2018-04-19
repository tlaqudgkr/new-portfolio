from django.db import models
import os


# Create your models here.

class Tourist(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    zoom = models.PositiveSmallIntegerField(default=14)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.FileField(upload_to='images/%Y/%m/%d/', null=True, blank=True)
    tourist = models.ForeignKey(Tourist)

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.image.name