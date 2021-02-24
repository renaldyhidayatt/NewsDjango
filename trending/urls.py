from django.urls import path
from . import views

urlpatterns = [
    path("trending", views.trending_list, name="trending_list"),
    path("trending/add", views.trending_add, name="trending_add"),
    path("trending/delete/<int:pk>", views.trending_delete, name="trending_delete"),
]
