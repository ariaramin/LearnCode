from django.db import models
from course.models import Course

# Create your models here.


class Session(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    video = models.FileField(upload_to='static/session/videos', null=False)
    time = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']