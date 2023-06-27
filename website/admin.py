from django.contrib import admin
from .models import Record

#customize django admin
class CustomizeAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','address']
    search_fields = ['first_name','last_name','address']
    list_filter = ['first_name','last_name','address']
    list_display = ['first_name','last_name','address']
    list_editable = ['address']

# Don't Customize Admin
# admin.site.register(Record)
# CustomizeAdmin
admin.site.register(Record,CustomizeAdmin)