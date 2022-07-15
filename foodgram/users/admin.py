from django.contrib import admin

from .models import CustomUser, Follow


class CustomUSerAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'pk',
    )
    list_filter = ('username', 'email')
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'author',
    )
    list_filter = ('author',)
    empty_value_display = '-пусто-'


admin.site.register(CustomUser, CustomUSerAdmin,)
admin.site.register(Follow, FollowAdmin)
