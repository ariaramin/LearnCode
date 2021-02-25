from django.contrib import admin
from .models import Instructor


# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    list_filter = ('date_joined',)


admin.site.register(Instructor, InstructorAdmin)