from django.contrib import admin

from apitest.models import Apistep,Apitest

# Register your models here.

class ApistepAdmin(admin.ModelAdmin):
    list_display=['apiname','apiurl','apiparamvalue','apimethod','apiresut','apistatus','creat_time','id','apitest']
    model=Apistep
    extra=1
    
class ApitestAdmin(admin.TabularInline):
    list_dispaly=['apitestname',' apitester','apitestresult','creat_time','id']
    inlines=[ApistepAdmin]



admin.site.register('ApitestAdmin','ApistepAdmin')

    