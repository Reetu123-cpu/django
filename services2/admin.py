from django.contrib import admin
from services2.models import student
# Register your models here.
class Serviceadmin2(admin.ModelAdmin):
    List_display=('name','age','marks','email','address')
admin.site.register(student,Serviceadmin2)

# Register your models here.
