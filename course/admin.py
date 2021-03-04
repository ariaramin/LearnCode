from django.contrib import admin
from .models import Course


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'price', 'status',)
    search_fields = ('title',)
    list_filter = ('created_at', 'status',)


admin.site.register(Course, CourseAdmin)
