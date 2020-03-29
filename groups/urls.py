from django.conf.urls import urls
from . import views


app_name = 'groups'

urlpatterns = [

url(r'^$', views.ListGroup.as_view(), name='list_group'),
url(r'^crete/$', views.CreateGroup.as_view(), name='create'),
url(r'^posts/in/(P?<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single')

]
