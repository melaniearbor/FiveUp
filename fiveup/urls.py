from django.conf.urls import patterns, include, url
from django.contrib import admin
import messagebox.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fiveup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url for adding a new message with a certain uuid as
    # a way to store for a certain user in the messages db
    url(r'^new/(?P<uuid>.+)/$', messagebox.views.CreateMessageView.as_view(),
    name='add-message-view',),
    url(r'^success/', messagebox.views.CreateMessageView.as_view(), 
    	name='add-message-success',),
)
