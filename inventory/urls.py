from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.view_item, name='view_item'),
    path('add_item/', views.add_item, name='add_item'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
    path('edit_item/<int:id>/', views.edit_item, name='edit_item'),
    path('edit_supplier/<int:id>/', views.edit_supplier, name='edit_supplier'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('update_item_amount/<int:id>/', views.update_item_amount, name='update_item_amount'),
]