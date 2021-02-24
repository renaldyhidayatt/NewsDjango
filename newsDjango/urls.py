"""newsDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls.conf import include


urlpatterns = [
    path("", include("main.urls")),
    path("", include("blacklistIp.urls")),
    path("", include("cat.urls")),
    path("", include("subcat.urls")),
    path("", include("trending.urls")),
    path("", include("news.urls")),
    path('', include('newsletter.urls')),
    path('', include('comments.urls')),
    path('', include('contactform.urls')),
    path("auth/", include("authenticate.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
