from django.conf.urls import url

from . import views

app_name = 'guiaTurismo'

urlpatterns = [
    url(r'^guide$', views.guides_view, name='guides'),
    url(r'^tour$', views.ToursList.as_view(), name='tours'),
    url(r'^city$', views.cities_view, name='city'),
    url(r'^city/(?P<city_id>\d+)/$', views.cities_view, name='cities'),
    url(r'^category$', views.categories_view, name='category'),
    url(r'^category/(?P<category_id>\d+)/$', views.categories_view, name='categories'),
    url(r'^sendEmail', views.email_view, name='email'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^isLogged/$', views.is_logged_view, name='isLogged'),

]