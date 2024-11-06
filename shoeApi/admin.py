from django.contrib import admin
from .models import *

class BaseProductAdmin(admin.ModelAdmin):
    """
    Base admin class for product models with common configurations.
    """
    search_fields = ['id', 'name']

# Concrete admin classes inheriting from the base class
@admin.register(MenModel)
class MenAdmin(BaseProductAdmin):
    pass

@admin.register(WomenModel)
class WomenAdmin(BaseProductAdmin):
    pass

@admin.register(KidsModel)
class KidsAdmin(BaseProductAdmin):
    pass

@admin.register(NewArrivalModel)
class NewArrivalAdmin(BaseProductAdmin):
    pass
