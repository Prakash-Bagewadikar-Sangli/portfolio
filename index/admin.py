from django.contrib import admin

from .models import Contact

# Register your models here.
admin.site.register(Contact)
class contactadmin(admin.ModelAdmin):
    list_display=['name','email','phone','concern']
