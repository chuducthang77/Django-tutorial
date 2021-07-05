from typing import Text
from django.db import models
from django.db.models.fields import CharField
from sorl.thumbnail import  ImageField

# Create your models here.
class Post(models.Model):
    text =  models.CharField(max_length=140, blank=False, null=False)
    image = ImageField()

    def __str__(self):
        return self.text