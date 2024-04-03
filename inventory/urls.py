from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.view_item, name='view_item'),
    path('add/', views.add_item, name='add_item'),
]