# from main import views
from news.views import news_add, news_delete, news_list, news_publish, news_update, news_detail, news_all_show, Testing, news_detail_short
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path("news/", news_list, name="news_list"),
    url(r'^news/(?P<word>.*)/$', news_detail, name='news_detail'),
    path("news/add", news_add, name="news_add"),
    path("news/edit/<int:pk>", news_update, name="news_update"),
    path("news/delete/<int:pk>", news_delete, name="news_delete"),
    path("news/publish/<int:pk>", news_publish, name="news_publish"),
    path('all/news/<word>', news_all_show, name="news_all_show"),
    path('testing/<username>', Testing, name="testing"),
    path('urls/<int:pk>', news_detail_short, name="news_detail_short")
]
