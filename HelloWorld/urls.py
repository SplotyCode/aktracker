"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin

from myweb import views as myweb_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^upload', myweb_views.uploadImg),
    re_path(r'^show/$', myweb_views.showImg),
    re_path(r'^artupload', myweb_views.uploadArt),
    re_path(r'^musupload', myweb_views.uploadMus),
    re_path(r'^vidupload', myweb_views.uploadVideo),
    re_path(r'^show/(\S+)/(\S+)/$', myweb_views.exshow),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
