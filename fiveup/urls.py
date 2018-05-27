from django.conf.urls import patterns, include, url
from django.contrib import admin
import messagebox.views
import fuauth.views
import fuauth.forms
from .views import display_cert

urlpatterns = patterns(
    '',
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', fuauth.forms.PublicUserCreation.as_view(),
        name='home',),
    url(r'^new/(?P<uuid>.+)/$', messagebox.views.CreateMessageView.as_view(),
        name='add-message-view',),
    url(r'^add-message-success/', messagebox.views.success,
        name='add-message-success',),
    url(r'^signup/', fuauth.forms.PublicUserCreation.as_view(),
        name='signup-form',),
    url(r'^register/', fuauth.views.register,
        name='register',),
    url(r'^loginuser/', fuauth.views.login_user,
        name='loginuser',),
    url(r'^logoutuser/', fuauth.views.logout_user,
        name='logoutuser',),
    url(r'^changeprofile/(?P<uuid>.+)/$', fuauth.forms.FiveUUserChangeForm.as_view(),
        name='changeprofile',),
    url(r'^contact/', messagebox.views.contact,
        name='contact',),
    url(r'^.well-known/pki-validation/BA7CD11C05866445FBFE053E2C1AAA8C.txt', display_cert),
)

STATIC_URL = '/static/'
