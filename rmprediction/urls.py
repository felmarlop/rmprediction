'''
Created on 28 de oct. de 2015

@author: PC1
'''
from django.conf.urls import url
from . import views 


urlpatterns = [
        url(r'^$', views.predict_Match),
        url(r'^match/(?P<pk>[0-9]+)/$', views.match_Detail),
        url(r'^match/new/$', views.match_new, name='match_new'),
]
