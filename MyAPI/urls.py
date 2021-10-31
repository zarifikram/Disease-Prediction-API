from django.urls import path
from . import views

urlpatterns = [
    path('predict', views.getPrediction),
    path("index", views.index),
]
