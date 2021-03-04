from django.contrib.auth.models import User
from django.db import models
from session.models import Session


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
    image = models.ImageField(upload_to='static/course/images/', null=False)
    level = models.CharField(max_length=5, choices=LEVEL)
    price = models.DecimalField(max_digits=7, decimal_places=0, default=0)
    status = models.CharField(max_length=5, choices=STATUS)
    session = models.ManyToManyField(Session)
    students = models.ManyToManyField(User, related_name='Student')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {self.title}

    class Meta:
        ordering = ['-created_at']

    objects = CourseManager()
