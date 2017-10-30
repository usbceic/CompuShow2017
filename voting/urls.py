#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  			   - URL configuration file.   			#
#                                                   #
#####################################################


from django.conf.urls import url

from . import views

app_name = 'voting'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^nominate/$', views.nominate, name='nominate'),
	url(r'^info/$', views.get_student_info, name='get_student_info'),
	url(r'^vote/$', views.vote, name='vote'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^login/$', views.log_in, name='log_in'),
	url(r'^logout/$', views.log_out, name='log_out'),
	url(r'^delete_nomination/$', views.delete_nomination, name='delete_nomination'),
	url(r'^make_nomination/$', views.make_nomination, name='make_nomination'),
]