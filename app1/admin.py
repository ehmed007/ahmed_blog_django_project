from django.contrib import admin
from .models import contact, blogs
# Register your models here.

class contact_data(admin.ModelAdmin):
    list_display = ('id','email','address','city','comments')

class blog_data(admin.ModelAdmin):
    list_display = ('title','description')


admin.site.register(contact, contact_data) 
admin.site.register(blogs, blog_data)