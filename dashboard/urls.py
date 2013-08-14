"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('dashboard.views',
    url(r'^$', 'dashboard', name='dashboard'),
    
)
