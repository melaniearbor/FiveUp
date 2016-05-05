from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin #as AuthUserAdmin

from fuauth.models import User
from fuauth.forms import FUserCreationForm #FUserChangeForm
from messagebox.models import Message
from messagevault.models import CuratedMessage
from messagevault.views import CuratedMessageForm
from courier.models import UserSendTime


class CustomUserAdmin(admin.ModelAdmin):

	add_form = FUserCreationForm

	readonly_fields = ('date_joined', 'uuid')

	fieldsets = (
		(None, {'fields': ('email', 'password', 'receive_newsletter')}),
		('Personal info', {'fields': ('name', 'phone_number', 'carrier', 'user_timezone')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'receiving_messages')}),
		('Auto info', {'fields': ('date_joined', 'uuid')}),
	)

	list_display = ('email', 'name', 'phone_number', 'is_active', 'is_staff',
		'receive_newsletter', 'receiving_messages', 'get_carrier_display')
	list_editable = ('is_active', 'receive_newsletter', 'receiving_messages')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',
		'receive_newsletter', 'receiving_messages', 'carrier')
	search_fields = ('email', 'name', 'phone_number', 'carrier')
	ordering = ('email', 'name')
	# filter_horizontal = (,)

class CuratedMessageAdmin(admin.ModelAdmin):

    add_form = CuratedMessageForm

    fieldsets = (
    	('Banana Town', {'fields': ('message_text', 'message_author_first', 'message_author_last')}),
	)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Message)
admin.site.register(CuratedMessage, CuratedMessageAdmin)
admin.site.register(UserSendTime)