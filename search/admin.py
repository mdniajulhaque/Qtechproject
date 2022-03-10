from django.contrib import admin
from .models import serch_key
@admin.register(serch_key)
class serch_keyModelAdmin(admin.ModelAdmin):
    list_display = ['id','search_keyword','used_search_engine',
    'what_results','what_time','what_date','date_time']
