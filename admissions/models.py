from pydoc import classname
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=1000)
    fathername =models.CharField(max_length=1000)
    classnames =models.IntegerField()
    contact =models.CharField(max_length=1000) 
