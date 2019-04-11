from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    #Personales
    url(r'^$', views.home, name='home'),
    url(r'^(?P<origen_id>\d+)$', views.home, name='home'),
    path('origen/<int:padre_id>/max/<int:max_child>/', views.home_limit, name='home_limit'),

    #Edicion
    path('crear_hijo/<int:id_padre>/', views.crear_sub_org, name='crear_sub_org'),
    
    #Web Services
    path('ws_org/', views.ws_org, name='ws_org'),
    path('ws_org/origen/<int:padre_id>/max/<int:max_child>/', views.ws_org_max, name='ws_org_max'),
    path('ws_func/', views.ws_func, name='ws_func'),
]