
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
     path('signup', views.signup,name="signup"),
     path('login', views.login,name="login"),
     path('display', views.display,name="display"),
     path('logout', views.logout,name="logout"),
     # path('loginWithKey', views.loginWithKey,name="loginWithKey"),
]
