from django.db import models

from sqlite3 import Date
from turtle import title
from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=200)

class Project(models.Model):
    serv = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=3000)
    fechaIni = models.DateField(default = Date.today)


