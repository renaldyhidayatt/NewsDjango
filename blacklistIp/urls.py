from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/blacklist/", views.back_list, name="blacklist"),
    path("dashboard/blacklist/add", views.ip_add, name="ip_add"),
    path("dashboard/blacklist/del/<int:pk>", views.ip_del, name="ip_del"),
]
