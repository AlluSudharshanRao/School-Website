from django.contrib import admin
from admissions.models import student

class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classnames','contact']
# Register your models here.
admin.site.register(student,studentAdmin)