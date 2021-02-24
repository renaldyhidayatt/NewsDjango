# from .views import AdminCkEditor, HomePage
from django.urls import path
from . import views
# from main.views import about_setting, site_setting, home

urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path("sitesetting/", views.site_setting, name="site_setting"),
    path("aboutsetting/", views.about_setting, name="about_setting")
    # path("ckeditor/", AdminCkEditor, name="ckeditorname")
    # path("dashboard/", adminPage, name="adminpage"),
    # path("dashboard/profile", adminProfilePage, name="adminProfilePage"),
    # path("dashboard/tables", adminTablePage, name="admintable"),
]
