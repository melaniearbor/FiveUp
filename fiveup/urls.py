from django.conf.urls import patterns, include, url
from django.contrib import admin
import messagebox.views
import fuauth.views
import fuauth.forms

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fiveup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', messagebox.views.index,
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
)

STATIC_URL = '/static/'
