from django.db import models

# Create your models here.

class CreateNewAccount(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class MenApi(models.Model):
    name=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    description=models.CharField(max_length=150)
    image=models.CharField(max_length=400)

class WomenApi(models.Model):
    name=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    description=models.CharField(max_length=150)
    image=models.CharField(max_length=400)

class KidsApi(models.Model):
    name=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    description=models.CharField(max_length=150)
    image=models.CharField(max_length=400)

class NewArrivalApi(models.Model):
    name=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    description=models.CharField(max_length=150)
    image=models.CharField(max_length=400)
    