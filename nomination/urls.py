#####################################################
#                                                   #
#       CompuSoft - The Compushow 2017 Software     #
#                                                   #
#####################################################
#                                                   #
#  - URL configuration file of nomination module.   #
#                                                   #
#####################################################


from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]