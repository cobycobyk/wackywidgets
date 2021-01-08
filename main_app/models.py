from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Widget(models.Model):
  description = CharField(max_length=50)
  quantity = IntegerField()