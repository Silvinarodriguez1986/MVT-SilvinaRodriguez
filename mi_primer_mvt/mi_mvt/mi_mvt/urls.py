"""mi_mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include
from familia import views
from familia.views import template_loader




urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world),
    path('title/', views.title),
    path('her-name-is/<str:nombre>/<int:edad>/', views.her_name_is),
    path('my-template/<str:nombre>/<str:apellido>/<str:relacion>/<str:nacimiento>/<int:edad>/', views.my_template),
    path('count/', views.count),
    path('template-loader/<str:nombre>/<str:apellido>/<str:relacion>/<str:nacimiento>/<int:edad>/', template_loader), 
    path("familia/", include("familia.urls")) 

   

]
