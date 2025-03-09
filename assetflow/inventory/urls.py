from django.urls import path
from .views import inventory_list_view, inventory_create_view, inventory_create_update_view, inventory_delete_view

urlpatterns = [
    path('list-inventory/', inventory_list_view, name='list_inventory'),
    path('create-inventory/', inventory_create_view, name='create_inventory'),
    path('update-inventory/<int:id>/', inventory_create_update_view, name='update_inventory'),
    path('delete-inventory/<int:id>/', inventory_delete_view, name='delete_inventory'),
]
