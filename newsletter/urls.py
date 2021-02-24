from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/add/', views.news_letter, name="news_letter"),
    path('dashboard/newsletter/email', views.news_emails, name="news_email"),
    path('dashboard/newsletter/phones', views.news_phone, name="news_phone"),
    path('dashboard/newsletter/delete/<int:pk>/<int:num>', views.news_txt_del, name="news_txt_del")
]