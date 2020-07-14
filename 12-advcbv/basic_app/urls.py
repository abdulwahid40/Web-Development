# -*- coding: utf-8 -*-
from django.conf.urls import url
from basic_app import views
from django.urls import path, re_path

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(), name='list'),
    re_path('^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(), name='detail'),
    re_path('^create/$', views.SchoolCreateView.as_view(), name='create'),
    re_path('^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(), name='update'),
    re_path('^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(), name='delete'),
    ]
#'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'