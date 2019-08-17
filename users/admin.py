from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class UsersAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'is_staff',
        'first_name',
        'last_name',
        'phone',
        'address'

    )
    list_filter = (
        'username',
        'email',
        'is_staff',
        'first_name',
        'last_name',
        'phone',
        'address'

    )
    fieldsets = UserAdmin.fieldsets


# Register your models here.
admin.site.register(User, UsersAdmin)