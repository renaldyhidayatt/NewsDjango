# from cat import views
from django.urls import path
from . import views

urlpatterns = [
    path("subcat/", views.subcatList, name="subcat_list"),
    path("subcat/add", views.subAdd, name="subcat_add"),
    path("subcat/delete/<int:pk>", views.subDelete, name="subcat_delete"),
]
