
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
     path('index', views.index,name="index"),
     path('login', views.login,name="login"),
     path('signup', views.signup,name="signup"),
     path('logout', views.logout,name="logout"),
     path('profile', views.profile,name="profile"),
     path('requests', views.requests,name="requests"),
     path('notifications', views.notifications,name="notifications"),
     path('updatestatus', views.updatestatus,name="updatestatus"),
     path('report', views.report,name="report"),
     
]
