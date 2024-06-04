from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    usertype=models.CharField(max_length=20)



class Panchayat(models.Model):
    name=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    wno=models.CharField(max_length=20)
    hno=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    president=models.CharField(max_length=20)
    add=models.CharField(max_length=100)
    con=models.BigIntegerField()
    
    

class Doctors(models.Model):
    name=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    add=models.CharField(max_length=100)
    dphnu=models.BigIntegerField()
    panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE,max_length=20)
    qual=models.CharField(max_length=20)
    opt=models.CharField(max_length=20)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)



class Workers(models.Model):
    name=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE,max_length=20)
    email=models.CharField(max_length=20)
    add=models.CharField(max_length=100)
    con=models.BigIntegerField()
    wan =models.CharField(max_length=20)
    qul=models.CharField(max_length=10)
   
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)

class Mothers(models.Model):
    wid=models.ForeignKey(Workers,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE,max_length=20)
    wno=models.IntegerField(null=True)
    add=models.CharField(max_length=100)
    con=models.BigIntegerField()
    pstatus=models.CharField(max_length=20,null=True)
    month=models.IntegerField(null=True)
    del_date=models.DateField(null=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)



class Projects(models.Model):
    valid=models.DateField(null=True)
    details=models.CharField(max_length=200)
    date=models.DateField(null=True)
    district=models.CharField(max_length=20)
    panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE,max_length=20)
    title=models.CharField(null=True,max_length=20)
    status=models.CharField(max_length=100)


    

class Vaccine(models.Model):
    
    district=models.CharField(max_length=20)
    panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE,max_length=20)
    title=models.CharField(null=True,max_length=20)
    con=models.CharField(null=True,max_length=20)
    add=models.CharField(null=True,max_length=200)
    valid=models.DateField(null=True)
    ward=models.CharField(max_length=100)
    time=models.TimeField(null=True)
    date=models.DateField(null=True)

class Foods(models.Model):
    
    district=models.CharField(max_length=20)
    panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE,max_length=20)
    needs=models.CharField(null=True,max_length=2000)
    con=models.CharField(null=True,max_length=20)
    add=models.CharField(null=True,max_length=200)
    date=models.DateField(null=True)
    ward=models.CharField(max_length=100)