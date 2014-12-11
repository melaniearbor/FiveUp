from django.conf.urls import patterns, include, url
from django.contrib import admin
import messages.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fiveup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url for adding a new message with a certain uuid as
    # a way to store for a certain user in the messages db
    url(r'^new/(?P<uuid>.+)/$', messages.views.CreateMessageView.as_view(),
    name='add-message-view',),
)
