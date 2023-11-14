from django.contrib import admin
from crudapp.models import book
# Register your models here.
class bookadmin(admin.ModelAdmin):
	list_display=['no','name','year','price']
admin.site.register(book,bookadmin)