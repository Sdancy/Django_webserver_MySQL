from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^content/$', views.content),
    url(r'^index/$', views.index),
    url(r'^add/$', views.add),
    url(r'^edit/$', views.edit),
    url(r'^delete/$', views.delete),
    url(r'^find/$', views.find),
    url(r'^v_index/$', views.v_index),
    url(r'^v_add/$', views.v_add),
    url(r'^v_edit/$', views.v_edit),
    url(r'^v_delete/$', views.v_delete),
    url(r'^v_find/$', views.v_find),
    url(r'^sign_up/$', views.sign_up),
    url(r'^u_index/$', views.u_index),
    url(r'^u_delete/$', views.u_delete),
    url(r'^u_v_add/$', views.u_v_add),
]