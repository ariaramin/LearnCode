from django.contrib import admin
from .models import Session


# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('created_at',)
    search_fields = ('title',)


admin.site.register(Session, SessionAdmin)