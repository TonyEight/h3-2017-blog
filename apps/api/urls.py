from django.conf.urls import url, include

from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'entries', views.EntryViewSet)

app_name = 'api'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls')),
]
