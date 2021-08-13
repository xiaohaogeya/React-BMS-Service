# coding=utf-8
from django.contrib import admin
from .models import CustomUser, Activity, Message, Product, Permission, Role

admin.site.site_header = 'react-admin后台管理'
admin.site.site_title = 'react-admin'


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    """
    用户模型
    """
    search_fields = ('name',)


