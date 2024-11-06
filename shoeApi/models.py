import uuid
from django.db import models

class BaseProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    image_url = models.URLField()
 
    class Meta:
        abstract = True  # This makes it an abstract base class

    def __str__(self):
        return self.name

# Concrete models that inherit from the base class
class MenModel(BaseProductModel):
    pass

class WomenModel(BaseProductModel):
    pass

class KidsModel(BaseProductModel):
    pass

class NewArrivalModel(BaseProductModel):
    pass
