from django.contrib import admin

from fuauth.models import User
from fuauth.forms import FUserCreationForm
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
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
            'receiving_messages', 'how_many_messages', 'interval_type')}),
        ('Auto info', {'fields': ('date_joined', 'uuid')}),
    )

    list_display = ('email', 'name', 'phone_number', 'receiving_messages',
        'how_many_messages', 'interval_type', 'date_joined', 'carrier')
    list_editable = ('receiving_messages',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',
        'receive_newsletter', 'receiving_messages', 'carrier')
    search_fields = ('email', 'name', 'phone_number', 'carrier')
    ordering = ('email', 'name')
    column = ('total_user_count',)

    def total_user_count(self, obj):
        return User.objects.count()

class CuratedMessageAdmin(admin.ModelAdmin):

    add_form = CuratedMessageForm

    fieldsets = (
        ('Banana Town', {'fields': ('message_text', 'message_author_first', 'message_author_last')}),
    )

    search_fields = ('message_author_last',)

class UserSendTimeAdmin(admin.ModelAdmin):

    list_display = ('user_name', 'user', 'scheduled_time', 'sent')

    search_fields = ('user__name', 'user__email', 'user__phone_number')

    ordering = ('user', 'scheduled_time', 'sent')

    list_filter = ('sent',)

    date_hierarchy = 'scheduled_time'

    def user_name(self, obj):
        return obj.user.name

    def user_email(self, obj):
        return obj.user.email




admin.site.register(User, CustomUserAdmin)
admin.site.register(Message)
admin.site.register(CuratedMessage, CuratedMessageAdmin)
admin.site.register(UserSendTime, UserSendTimeAdmin)
