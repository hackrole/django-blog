from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateField()

    def __unicode__(self):
        pass

    class Meta:
        pass
