from django.conf.urls import url
from . import views


urlpatterns = [
            url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
            url(r'^login/$', views.LoginFormView.as_view(), name='login'),
            url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
            # url(r'^login/$', views.login, name='login'),
            # url(r'^logout/$', views.logout, name='logout'),
            # url(r'^register/$', views.registration, name='register'),
]