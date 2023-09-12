# from django.contrib import admin
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .forms import UserChangeForm, UserCreationForm
# from .models import User

# class UserAdmin(BaseUserAdmin):
#   form = UserChangeForm
#   add_form = UserCreationForm

#   list_display = ('uid')
#   fieldsets = (
#     (None, {'fields': ('uid', 'password')}),
#   )

#   add_fieldsets = (
#     (None, {
#       'classes': ('wide',),
#       'fields': ('uid', 'pw', 'pw2')}
#     ),
#   )
#   search_fields = ('uid',)
#   ordering = ('uid',)
#   filter_horizontal = ()


# admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)