from django.contrib import admin
from category.models import Category


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    list_filter = ['created_at', ]
    search_fields = ['title', 'description']


admin.site.register(Category, CategoryAdmin)
