from django.db import models

class temp(models.Model):
    Name = models.CharField(max_length=250)

    DOB = models.DateField()

    Street = models.CharField(max_length=250,null=True)
    Locality = models.CharField(max_length=250,null=True)
    City = models.CharField(max_length=250,null=True)
    District = models.CharField(max_length=250,null=True)
    State = models.CharField(max_length=250,null=True)
    Pincode = models.CharField(max_length=8,null=True)
    UID = models.CharField(max_length=250,null=True,unique=True)

    def __str__(self):


        return self.Name

# Create your models here.
class Person(models.Model):
    Name=models.CharField(max_length=250)

    DOB=models.DateField()

    Street=models.CharField(max_length=250)
    Locality=models.CharField(max_length=250)
    City=models.CharField(max_length=250)
    District=models.CharField(max_length=250)
    State=models.CharField(max_length=250)
    Pincode=models.CharField(max_length=8)
    UID=models.CharField(max_length=250,primary_key=True)

    def __str__(self):
        return self.Name
