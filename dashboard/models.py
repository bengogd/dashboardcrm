from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_type(models.Model):
    is_manager = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    





