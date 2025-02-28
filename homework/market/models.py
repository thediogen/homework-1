import datetime

from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.CharField(max_length=100)


    @property
    def age(self):
        _age = int((datetime.date.today() - self.birthday).days/365.25)

        return _age
