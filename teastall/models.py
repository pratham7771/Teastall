from django.db import models


# Create your models here.

class signupuser(models.Model):
    stfirstname=models.CharField(max_length=30)
    stlastname=models.CharField(max_length=30)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    cpassword=models.CharField(max_length=20)
    stcity=models.CharField(max_length=30)
    mo=models.BigIntegerField()
    selectimages=models.FileField(upload_to='Myimages',blank=True)
    gender=models.CharField(max_length=15)

    def __str__(self):
        return self.stfirstname

class paymentuser(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=60)
    cardname=models.CharField(max_length=90)
    cardnumber=models.BigIntegerField()
    expmonth=models.CharField(max_length=90)
    expyear=models.IntegerField()
    cvv=models.IntegerField()
    cpay=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class usersuggestion(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    subject=models.TextField()
    feedback=models.TextField()
    nameofuploader=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class contactuser(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.EmailField()
    message=models.TextField()
    cuser=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
