from django.db import models
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()



class GunImage(models.Model):
    file = models.ImageField(storage=fs,upload_to='')
# Create your models here.
class user(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
            db_table="user"

class Region(models.Model):
    attack_place = models.CharField(max_length=20)
    ground_image = models.ImageField(upload_to='thermal_images/')
    enemy_image = models.ImageField(upload_to='thermal_images/')
    class Meta:
            db_table="Region"
