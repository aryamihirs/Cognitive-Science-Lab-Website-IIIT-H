from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^home$', views.home, name='home'),
	url(r'^about', views.about, name='about'),
	url(r'^posts/(?P<page_number>[0-9]+)/$', views.posts, name='posts'),
	url(r'^posts/$', views.redirect_posts, name='redirect_posts'),	
	url(r'^posts/details/(?P<post_number>[0-9]+)/$', views.details, name='details'),
	url(r'^name', views.get_name, name='get_name'),
	url(r'^volunteer', views.volunteer, name='volunteer'),
	url(r'^contact', views.contact, name='contact'),
	url(r'^videos', views.videos, name='videos'),
	url(r'^gallery', views.gallery, name='gallery'),	
]
