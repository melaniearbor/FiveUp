from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from fuauth.models import User
from fuauth.forms import UserCreationForm, UserChangeForm

# Register your models here.

class UserAdmin(AuthUserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password', 'receive_newsletter')}),
		('Personal info', {'fields': ('name', 'phone', 'carrier', 'timezone')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
			'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {'fields': ('email', 'password1', 'password2', 'recieve_newsletter')}),
		('Personal info', {'fields': ('name', 'phone', 'carrier', 'timezone')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
	)
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('email', 'name', 'phone_number', 'is_active', 'is_staff',
		'receive_newsletter')
	list_editable = ('is_active', 'receive_newsletter')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',
		'receive_newsletter')
	search_fields = ('email', 'name', 'phone_number')
	ordering = ('')

admin.site.register(User, UserAdmin)