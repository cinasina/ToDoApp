from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User, Profile
from .forms import GroupAdminForm


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_active', 'is_superuser',)
    list_editable = ('is_active',)
    list_filter = ('is_active', 'is_superuser',)
    search_fields = ('email',)
    ordering = ('email',)
    """Showing User Fields In Admin Panel"""
    fieldsets = [
        (None, {"fields": ["email", "password", 'last_login', ]}),
        ("Personal Info", {"fields": []}),
        ("Permissions", {"fields": ['is_staff', 'is_active', "is_superuser", 'is_verified']}),
        ("Group Permission", {"fields": ['user_permissions']}),
    ]
    """Add New User In Admin Panel And Show The Needed Form"""
    add_fieldsets = [
        (None, {"classes": ["wide"],
                "fields": ["email", "password1", 'password2', 'is_active', 'is_staff', 'is_superuser',
                           'is_verified', ], },),
    ]


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ['permissions']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
