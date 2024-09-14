from django.contrib import admin

from .models import *

class MenAdmin(admin.ModelAdmin):
    search_fields=['id','name']

class WomenAdmin(admin.ModelAdmin):
    search_fields=['id','name']

class KidsAdmin(admin.ModelAdmin):
    search_fields=['id','name']

class NewArrivalAdmin(admin.ModelAdmin):
    search_fields=['id','name']

admin.site.register(MenModel,MenAdmin)
admin.site.register(WomenModel,WomenAdmin)
admin.site.register(KidsModel,KidsAdmin)
admin.site.register(NewArrivalModel,NewArrivalAdmin)