from django.contrib import admin

from .models import Api

@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
    list_display = ('name' , 'author' ,'size' , 'created')
    list_filter = ('name' , 'author')


