from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Personales
    url(r'^$', views.home, name='home'),

    path('crear_hijo/<int:id_padre>/', views.crear_sub_org, name='crear_sub_org'),
    
    #Web Services
    url('ws_org/', views.ws_org, name='ws_org'),
    url('ws_func/', views.ws_func, name='ws_func'),
]