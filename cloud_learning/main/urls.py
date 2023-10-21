"""
URL configuration for cloud_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index, name= 'index'),
    path("logout/", views.logout_request, name='logout'),
    path("blog_detail/<int:id>", views.blog_detail, name='blog_detail'),
    path('pag/',views.pagination, name= 'pagination'),
    path('playbook/',views.playbook,name='playbook'),
    path('adduser/',views.adduser,name='adduser'),
    path('deleteuser/',views.deleteuser,name='deleteuser'),
    path('lockuser/',views.lockuser,name='lockuser'),
    path('install_sw/',views.install_sw,name='install_sw'),
    path('remove_sw/',views.remove_sw,name='remove_sw'),
    path('provision_cluster/',views.provision_cluster,name='provision_cluster'),
    path('deprovision_cluster/',views.deprovision_cluster,name='deprovision_cluster'),
    path('addinventory/',views.addinventory,name='addinventory'),
    path('taginventory/',views.taginventory,name='taginventory'),
    
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
