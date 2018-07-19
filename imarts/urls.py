from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as imarts_views
urlpatterns =[

	url(r'^$', imarts_views.home, name ='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	#url(r'^signup/$', student_views.signup, name='signup'),
	url(r'^signup_success/$', imarts_views.signup_success, name ='signup_success'),
    url(r'^search/$', imarts_views.search, name='search'),
    url(r'^buy/$', imarts_views.buy, name='buy'),
    url(r'^cat/$', imarts_views.cat, name='cat'),
    url(r'^chart/$', imarts_views.test_matplotlib, name='chart'),
    url(r'^bargraph/$', imarts_views.bargraph, name='bargraph'),

]
