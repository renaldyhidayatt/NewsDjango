from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/cat/", views.cat_list, name="cat_list"),
    path("dashboard/cat/add", views.CatAdd, name="cat_add"),
    path("dashboard/cat/delte/<int:pk>", views.cat_del, name="cat_del"),
    path("dashboard/cat/export-csv", views.export_cat_csv, name="export_cat_csv"),
    path("dashboard/cat/import-csv", views.import_cat_csv, name="import_cat_csv"),
]
