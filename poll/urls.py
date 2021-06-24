from django.urls import path
from .import views
urlpatterns = [

    path('', views.index, name="index" ),
    path('poll/details/<int>:id', views.details, name="details"),

    path('poll/results', views.results, name="results"),
    path('poll/prefer', views.prefer, name="prefer")
]