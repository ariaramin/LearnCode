from django.db import models
from user.models import Account


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150, null=False, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='article/image', null=False)
    author = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
