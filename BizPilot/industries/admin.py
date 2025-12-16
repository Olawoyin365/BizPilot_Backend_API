from django.contrib import admin
from .models import Industry

@admin.register(Industry)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

