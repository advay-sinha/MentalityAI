from django.contrib import admin
from .models import MoodLog

@admin.register(MoodLog)
class MoodLogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'pmood', 'timestamp')  # Columns displayed in the admin
    search_fields = ('name', 'pmood')                     # Fields that can be searched in admin
    list_filter = ('pmood', 'timestamp')                  # Filter options in admin sidebar
    ordering = ('-timestamp',)                            # Default ordering of records (latest first)
