from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('addTwo',views.addTwo),
    path('reset',views.reset)
]