from django.contrib import admin
# from django.contrib.auth.models import User
from sign.models import Event, Guest, User
# Register your models here.
# admin.site.register(Event)
# admin.site.register(Guest)
'''
class ProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name = 'profile'

class UserAdmin(admin.ModelAdmin):
   inlines = ()
'''

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    # 搜索栏
    search_fields = ['name']
    # 过滤器
    list_filter = ['status']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']
    list_filter = ['sign']

admin.site.register(User)
admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)