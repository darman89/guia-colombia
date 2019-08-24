from django.conf.urls import url

from . import views

app_name = 'guiaTurismo'

urlpatterns = [
    url(r'^guides$', views.guides_view, name='guides'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^isLogged/$', views.is_logged_view, name='isLogged'),

]