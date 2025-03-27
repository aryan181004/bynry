# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

import random
import string

def generate_account_number():
    while True:
        # Generate a random 10-digit number
        account_number = ''.join(random.choices(string.digits, k=10))
        # Check if this account number already exists
        if not Customer.objects.filter(account_number=account_number).exists():
            return account_number

class Customer(AbstractUser):
    account_number = models.CharField(max_length=10, unique=True, default=generate_account_number)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
