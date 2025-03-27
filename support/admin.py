from django.contrib import admin
from .models import SupportNote

@admin.register(SupportNote)
class SupportNoteAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'support_rep', 'created_at')
    list_filter = ('created_at', 'support_rep')
    search_fields = ('note', 'service_request__customer__username')