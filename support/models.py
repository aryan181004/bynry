# support/models.py
from django.db import models
from django.conf import settings
from service_requests.models import ServiceRequest

class SupportNote(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='support_notes')
    support_rep = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for Request {self.service_request.id} by {self.support_rep.username}"
