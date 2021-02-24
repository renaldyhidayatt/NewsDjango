from django.urls import path
from . import views

urlpatterns = [
    path('comments/add/news/<int:pk>', views.news_cm_add, name="news_cm_add"),
    path('dashboard/comments/', views.comments_list, name="comments_list"),
    path('dashboard/comments/del/<int:pk>', views.comments_del, name="comments_del"),
    path('dashboard/comments/confirme/<int:pk>', views.comments_confirme, name="comments_confirme")
]