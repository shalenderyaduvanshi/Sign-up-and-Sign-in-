from . import views
from django.urls import path

urlpatterns=[
    path('', views.index),
    path('/signup/', views.signup),
    path('signup_output/', views.signup_output),
    path('/signin/', views.login),
]

