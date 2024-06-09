from django.db import models

# Create your models here.
class About(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    dob_me = models.DateField(null=True)
    about = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to='images/')

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(null=True)
    message = models.TextField(null=True)
    date = models.DateField(null=True)
