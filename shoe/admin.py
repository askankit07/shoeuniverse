from django.contrib import admin

from .models import *

class CustomerAdmin(admin.ModelAdmin):
    search_fields=['first_name','last_name','email']

class OrderAdmin(admin.ModelAdmin):
    search_fields=['productName','productId','orderId']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)

