from django.urls import path
from . import views

urlpatterns = [
    path('contact/submit/', views.contact_add, name="contact_add"),
    path('dashboard/contactform', views.contact_show, name="contact_show"),
    path('dashboard/contactform/del/<int:pk>', views.contact_del, name="contact_del")
]