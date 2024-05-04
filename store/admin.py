from django.contrib import admin
from . import models
import datetime

# admin.site.register(models.Customer, CustomerAdmin)
# Instead of above line we could de:

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_editable = ['last_name']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    
    def is_under_18(self, customer):
        return 'YES'

    
    list_display = ['first_name', 'last_name', 'is_under_18']

admin.site.register(models.Order)
