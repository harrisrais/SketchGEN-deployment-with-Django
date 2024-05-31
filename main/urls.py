from django.urls import path
from . import views

urlpatterns =[
    path("",view=views.index,name="index"),
    path("sketch",view=views.sketch,name="sketch")
]