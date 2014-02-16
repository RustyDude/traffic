from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
	url(r'^intersections/$', 'intersections.views.intersections'),
	url(r'^', 'intersections.views.login_user'),
)
