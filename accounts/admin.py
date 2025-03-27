from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer

class CustomerAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'account_number')
    search_fields = ('username', 'email', 'account_number')
    list_filter = ('is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Customer Information', {'fields': ('phone_number', 'address', 'account_number')}),
    )

admin.site.register(Customer, CustomerAdmin)