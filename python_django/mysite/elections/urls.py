
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^area/(?P<area>.+)/results$',views.results),
    url(r'^area/(?P<area>.+)/$',views.areas),
    url(r'^polls/(?P<poll_id>\d+)/$',views.polls),
    #url(r'^candidates/(?P<name>[가-힣]+)/$',views.candidates)
]
