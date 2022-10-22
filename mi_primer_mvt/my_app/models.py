
from django.db import models

# Create your models here.
class Familia(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    relation = models.CharField(max_length=40)
    profession = models.CharField(max_length=40)
    age = models.IntegerField()
  

    def __str__(self):
        return f"{self.name} - {self.last_name} - {self.relation} - {self.profession} - {self.age}"



   