from django.db import models


# Create your models here.

class info(models.Model):
    Username = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)
    Firstname = models.CharField(max_length=25)
    Lastname = models.CharField(max_length=25)
    Age = models.DateField()
    Date_Of_Birth = models.IntegerField()
    Gender = models.CharField(max_length=15)
    class Meta:
        db_table = 'info'
