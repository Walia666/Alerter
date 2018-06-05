from django.conf.urls import url
from . import views

urlpatterns =[	
	url(r'^$',views.dashboard,name='test'),
	url(r'^form/$',views.form,name='form'),
	url(r'^login/',views.login,name='login'),
	url(r'^applogalert/$', views.applogalert, name='home'),
	url(r'^valid/$', views.valid, name='valid'),
	url(r'^elast/$', views.elast, name='elast'),
	url(r'^modify/$', views.modify, name='modify'),
	url(r'^edit/$', views.edit, name='edit'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^crossdomainData/$', views.crossdomainData, name='crossdomainData'),
	url(r'^generate/$', views.generate, name='generate'),
        url(r'^alertinfo/$', views.alertinfo, name='alertinfo'),
 	url(r'^docsnew/$', views.docsnew, name='docsnew'),
        url(r'^postpone/$', views.postpone, name='postpone'),


	
	url(r'^search/$', views.search, name='search')





 
	]

