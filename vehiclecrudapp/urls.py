from django.contrib import admin
from django.urls import path,include
from vehiclecrudapp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add',views.add,name='add'),
    path('update',views.update,name='update'),
    path('update/<str:id>',views.update),
    path('details',views.details,name='details'),
    path('list',views.list,name='list'),
    path('details/<str:id>',views.getdetails)
    
]
