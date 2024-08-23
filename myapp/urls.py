from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_list, name='producto_list'),
    path('nuevo/', views.producto_create, name='producto_create'),
    path('editar/<int:pk>/', views.producto_update, name='producto_update'),
    path('borrar/<int:pk>/', views.producto_delete, name='producto_delete'),
]
