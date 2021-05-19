from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account/images', default='account/images/user.png', null=True)


