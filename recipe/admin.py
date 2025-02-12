from django.contrib import admin
from recipe.models import rec
# Register your models here.
class rec2(admin.ModelAdmin):
    list_display=('Recepy_name','Description','Image')
admin.site.register(rec,rec2)