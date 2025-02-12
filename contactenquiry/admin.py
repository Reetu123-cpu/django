from django.contrib import admin
from contactenquiry.models import contactenquiry
# Register your models here.
from django.contrib import admin
from news.models import News
# Register your models here.
class contactenquiryadmin(admin.ModelAdmin):
    List_display=('name','email','phoneno','message')
admin.site.register(contactenquiry,contactenquiryadmin)