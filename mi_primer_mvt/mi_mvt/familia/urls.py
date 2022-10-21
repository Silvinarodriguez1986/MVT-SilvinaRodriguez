from django.urls import path
from . import views



urlpatterns = [
  
    path('hello-world/', views.hello_world), 
    path('title/', views.title),
    path('her-name-is/<str:nombre>/<int:edad>/', views.her_name_is),
    path('my-template/<str:nombre>/<str:apellido>/<str:relacion>/<str:nacimiento>/<int:edad>/', views.my_template),
    path('count/', views.count),
    #path('template-loader/<str:nombre>/<str:apellido>/<str:relacion>/<str:nacimiento>/<int:edad>/', template_loader), 
    path('familiaview/', views.familia),
 
]