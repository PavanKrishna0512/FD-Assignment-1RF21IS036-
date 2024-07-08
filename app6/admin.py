

from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fName', 'lName', 'Aadhaar', 'Pincode', 'CustId')
    search_fields = ('fName', 'lName', 'Aadhaar', 'CustId')
    readonly_fields = ('CustId',)

admin.site.register(Customer, CustomerAdmin)
