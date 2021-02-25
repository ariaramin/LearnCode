from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Instructor(User):
    image = models.ImageField(upload_to='instructor/images', default='instructor/images/user.png', null=False)

    def __str__(self):
        return self.username


