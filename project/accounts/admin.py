from django.contrib import admin
from .models import *
# Register your models here.

class ptd(admin.ModelAdmin):
    list_display = [ 'name' , 'doctor' , 'age' , 'phone1' , 'description']

class CRT (admin.ModelAdmin):
    list_display = ['title' , 'user' , 'time']

class FAVDTL(admin.ModelAdmin):
    list_display = ['user' , 'Post']

class Comment_dtl(admin.ModelAdmin):
    list_display = ['name' , 'post' , 'time']

admin.site.register(Profile)
admin.site.register(patient , ptd)
admin.site.register(Create_Post , CRT)
admin.site.register(Comment , Comment_dtl)
admin.site.register(Favorite , FAVDTL)