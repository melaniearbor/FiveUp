from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin #as AuthUserAdmin

from fuauth.models import User
from fuauth.forms import FUserCreationForm #FUserChangeForm
from messagebox.models import Message
from messagevault.models import CuratedMessage
from messagevault.views import CuratedMessageForm
from courier.models import UserSendTime

# Register your models here.

# class UserAdmin(AuthUserAdmin):

# 	form = FUserChangeForm
# 	add_form = FUserCreationForm

# 	readonly_fields = ('date_joined', 'uuid')
# 	fieldsets = (
# 		(None, {'fields': ('email', 'password', 'receive_newsletter')}),
# 		('Personal info', {'fields': ('name', 'phone_number', 'carrier', 'user_timezone')}),
# 		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
# 			'groups', 'user_permissions')}),
# 		('Important dates', {'fields': ('last_login', 'date_joined')}),
# 	)
# 	add_fieldsets = (
# 		(None, {'fields': ('email', 'password1', 'password2', 'receive_newsletter')}),
# 		('Personal info', {'fields': ('name', 'phone_number', 'carrier', 'user_timezone')}),
# 		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
# 		('Auto info', {'fields': ('date_joined', 'uuid')}),
# 	)

class CustomUserAdmin(admin.ModelAdmin):

	add_form = FUserCreationForm
	#form = FUserChangeForm

	readonly_fields = ('date_joined', 'uuid')
	# fieldsets = (
	# 	(None, {'fields': ('email', 'password', 'receive_newsletter')}),
	# 	('Personal info', {'fields': ('name', 'phone_number', 'carrier', 'user_timezone')}),
	# 	('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
	# 		'groups', 'user_permissions')}),
	# 	('Important dates', {'fields': ('last_login', 'date_joined')}),
	# )
	fieldsets = (
		(None, {'fields': ('email', 'password', 'receive_newsletter')}),
		('Personal info', {'fields': ('name', 'phone_number', 'carrier', 'user_timezone')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
		('Auto info', {'fields': ('date_joined', 'uuid')}),
	)

	list_display = ('email', 'name', 'phone_number', 'is_active', 'is_staff',
		'receive_newsletter')
	list_editable = ('is_active', 'receive_newsletter')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',
		'receive_newsletter')
	search_fields = ('email', 'name', 'phone_number')
	ordering = ('email', 'name')
	# filter_horizontal = (,)

class CuratedMessageAdmin(admin.ModelAdmin):

    add_form = CuratedMessageForm

    fieldsets = (
    	('Banana Town', {'fields': ('message_text', 'message_author_first', 'message_author_last')}),
	)

# class UserSendTime(admin.ModelAdmin):

# 	list_display = ('user', 'scheduled_times', 'sent')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Message)
admin.site.register(CuratedMessage, CuratedMessageAdmin)
admin.site.register(UserSendTime)