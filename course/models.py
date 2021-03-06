from django.contrib.auth.models import User
from django.db import models
from category.models import Category


# Create your models here.
class CourseManager(models.Manager):
    def published(self):
        return self.filter(status='pub')


class Course(models.Model):
    LEVEL = (
        ('beg', 'Beginner'),
        ('int', 'Intermediat'),
        ('adv', 'Advance'),
    )
    STATUS = (
        ('drf', 'Draft'),
        ('pub', 'Published')
    )
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='course/images/', null=False)
    level = models.CharField(max_length=5, choices=LEVEL)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    status = models.CharField(max_length=5, choices=STATUS)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

    objects = CourseManager()
