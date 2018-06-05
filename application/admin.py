from .models import  Dashboard,Tag,Log,Log_type,Alert
from django.contrib import admin
from django.contrib.sessions.models import Session


class StoreAdmin(admin.ModelAdmin):
	 
      list_display = ('Dashboard_name','Dashboard_url','owner_name','owner_email')
      search_fields=('Dashboard_name','Dashboard_url','owner_name','owner_email')
      list_filter = ('feature_type',)
    
      
admin.site.register(Dashboard, StoreAdmin)
admin.site.register(Tag)

class LogAdmin(admin.ModelAdmin):
	list_display=('index','ip_endpoint','log_field')
admin.site.register(Log,LogAdmin)
admin.site.register(Log_type)
admin.site.register(Alert)


