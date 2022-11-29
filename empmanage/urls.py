from django.contrib import admin
from django.urls import path, include

from empmanage import views

urlpatterns = [
    # path('', include('empmange.urls')),
    path('', views.loginpage, name='login'),
    path('empadd/', views.addempdet, name='empadd'),
    path('addsalarydet/', views.addsalarydet, name='addsalarydet'),
    
    path('emplist/', views.emplist, name='emplist'),
    path('empcreate/', views.empcreate, name='empcreate'),
    path('empupdate/<int:id>/', views.empupdate, name='empupdate'),
    path('deleteemp/<int:id>/', views.deleteemp, name='deleteemp'),
    
    path('logoutuser/', views.logoutuser, name='logoutuser'),

   
]
