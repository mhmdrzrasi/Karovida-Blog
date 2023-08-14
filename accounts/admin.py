from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm

from .models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["get_name", "is_editor", "is_journalist", "is_staff", "is_superuser", "id"]
    list_filter = ["is_superuser", "is_staff", "is_journalist", "is_editor"]

    fieldsets = [
        (None, {"fields": ["phone_number", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name", "national_id", "email"]}),
        ("Permissions", {"fields": ["is_editor", "is_journalist", "is_staff", "is_superuser", "user_permissions"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["first_name", "last_name", "phone_number", "national_id", "email", "password1", "password2",
                           "is_editor", "is_journalist", "is_active", "is_staff", "is_superuser", "user_permissions"],
            },
        ),
    ]
    search_fields = ["first_name", "last_name", "phone_number", "national_id"]
    ordering = ["first_name", "last_name"]
    filter_horizontal = ['user_permissions']

    def get_name(self, obj):
        return obj.get_short_name()

    get_name.short_description = "full name"


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
