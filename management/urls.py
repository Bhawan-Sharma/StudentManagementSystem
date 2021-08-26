"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from mirai import views
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 
from mirai.views import *
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    #Company paths 
    path('comp', views.comp),
    path('show', views.show),
    path('edit/<str:sName>', views.edit),
    path('update/<str:sName>', views.update),
    path('delete/<str:sName>', views.delete),

    #employee paths
    path('emp', views.emp),
    path('showemp', views.showemp),
    path('deleteEmp/<str:Name>', views.deleteEmp),
    path('editemp/<str:Name>', views.editemp),
    path('updateEmp/<str:Name>', views.updateEmp),

    #Homepage path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('main_view',views.main_view),
    #inbuilt login path
    path('accounts/', include('django.contrib.auth.urls')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
#for Media Storage 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 