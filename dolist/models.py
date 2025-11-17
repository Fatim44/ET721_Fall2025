from django.db import models

#Create your models here. 
class Todolist(models.Model):
    text - models.Charfield(max_length-100)
    completed - models.BooleanField(default-False)