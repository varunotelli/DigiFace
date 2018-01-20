from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^person/add/$',views.PersonCreate.as_view(success_url='/digiface/'),name='person-add'),
]