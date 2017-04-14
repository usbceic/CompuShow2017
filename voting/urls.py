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
	url(r'^mynominees/$', views.my_nominees, name='my_nominees'),
	url(r'^vote/$', views.vote, name='vote'),
	url(r'^myvotes/$', views.my_votes, name='my_votes'),
	url(r'^login/$', views.log_in, name='log_in'),
	url(r'^logout/$', views.log_out, name='log_out'),
]