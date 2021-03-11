from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, null=False, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='static/article/image', null=False)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
