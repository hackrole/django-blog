from django.db import models

# Create your models here.

class Cate(models.Model):
    name = models.CharField(max_length=20)
    is_show = models.BooleanField(default=False)
    
class Blog(models.Model):
    tilte = models.CharField(max_length=30)
    cate = models.ForeignKey(Cate)

class Tag(models.Model):
    name = models.CharField(max_length=30)
    blog = models.ManyToManyField(Blog)

