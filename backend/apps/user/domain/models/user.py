from statistics import mode
from django.db import models
from django.core.validators import RegexValidator

class User():
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True, validators=[RegexValidator(
        regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$',
        message='Wrong phone number format'
    )])
    email = models.EmailField(max_length=255, unique=True)
