from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from TravelingCompanion import settings
from companions import views
from registation.views import register

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/$', login_required(views.CreateView.as_view()), name='create'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(views.EditView.as_view()), name='edit'),
    url(r'^(?P<route_id>\d+)/imgoing/$', views.imGoing, name='imgoing'),
    url(r'^(?P<route_id>\d+)/imnotgoing/$', views.imNotGoing, name='imnotgoing'),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html', 'redirect_field_name': '/'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/logout.html', 'next_page': '/'}),
    url(r'^accounts/register/$', register, name='register'),
)
