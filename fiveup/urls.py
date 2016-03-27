from django.conf.urls import patterns, include, url
from django.contrib import admin
import messagebox.views
import fuauth.views
import fuauth.forms

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fiveup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', fuauth.forms.PublicUserCreation.as_view(),
        name='home',),
    # url for adding a new message with a certain uuid as
    # a way to store for a certain user in the messages db
    url(r'^new/(?P<uuid>.+)/$', messagebox.views.CreateMessageView.as_view(),
    name='add-message-view',),
    url(r'^add-message-success/', messagebox.views.success, 
    	name='add-message-success',),
    url(r'^signup-success/', fuauth.views.success, 
        name='signup-success',),
    url(r'^signup/', fuauth.forms.PublicUserCreation.as_view(),
        name='signup-form',),
    url(r'^register/', fuauth.views.register,
        name='register',),
    url(r'^test-signup/', fuauth.views.testsign, 
        name='test-signup',),
    url(r'^loginform/', fuauth.views.loginform, 
        name='loginform',),
    url(r'^loginuser/', fuauth.views.login_user, 
        name='loginuser',),
    url(r'^logoutuser/', fuauth.views.logout_user, 
        name='logoutuser',),
    url(r'^changeprofile/(?P<uuid>.+)/$', fuauth.forms.FiveUUserChangeForm.as_view(), 
        name='changeprofile',),
    url(r'^contact/', messagebox.views.contact, 
        name='contact',),
)

STATIC_URL = '/static/'
