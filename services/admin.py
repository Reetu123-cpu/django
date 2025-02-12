from django.contrib import admin
from services.models import Service
# Register your models here.
class Serviceadmin(admin.ModelAdmin):
    List_display=('service_icon','service_title','service_description')
admin.site.register(Service,Serviceadmin)