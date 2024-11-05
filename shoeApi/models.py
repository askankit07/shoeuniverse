import uuid
from django.db import models

class MenModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    imageUrl = models.URLField()
    
    def __str__(self):
        return self.name

class WomenModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    imageUrl = models.URLField()

    def __str__(self):
        return self.name

class KidsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    imageUrl = models.URLField()

    def __str__(self):
        return self.name

class NewArrivalModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    imageUrl = models.URLField()

    def __str__(self):
        return self.name
