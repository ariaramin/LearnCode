from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Student(User):
    image = models.ImageField(upload_to='static/student/images', default='static/img/user.png', null=False)

    def __str__(self):
        return self.username
