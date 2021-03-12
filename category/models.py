from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=120, null=False, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='static/category/image', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
