from django.db import models

# Create your models here.



class users(models.Model):
    objects = models.Manager()

    username = models.CharField(max_length=20,unique =True)
    psw = models.IntegerField()