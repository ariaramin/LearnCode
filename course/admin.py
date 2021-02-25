from django.contrib import admin
from .models import Course


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'price', 'instructor', 'status',)
    search_fields = ('title', 'instructor',)
    list_filter = ('created_at', 'instructor', 'status',)


admin.site.register(Course, CourseAdmin)
