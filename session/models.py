from datetime import timedelta

from django.db import models


# Create your models here.


class SessionManager(models.Manager):
    def Published(self):
        return self.filter(status='pub')


class Session(models.Model):
    STATUS = (
        ('drf', 'Draft'),
        ('pub', 'Published'),
    )
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    video = models.FileField(upload_to='session/videos', null=False)
    time = models.DurationField()
    status = models.CharField(max_length=5, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    object = SessionManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']