from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='category/static/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
