from django.conf.urls import url

from .views import (
	HomeView,
	CategoryIndexView,
	EntryDetailView
)

app_name = 'blog'
urlpatterns = [
    url(
    	r'^$',
    	HomeView.as_view(),
    	name='index'
    ),
    url(
    	r'^category/(?P<pk>[0-9]+)/$',
    	CategoryIndexView.as_view(),
    	name='category-index'
    ),
    url(
    	r'^article/(?P<pk>[0-9]+)/$',
    	EntryDetailView.as_view(),
    	name='entry-detail'
    ),
]