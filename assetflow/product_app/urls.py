from django.urls import path
from .views import product_list_view, product_create_view, product_create_update_view, product_delete_view

urlpatterns = [
    path('list-product/', product_list_view, name='list_product'),
    path('create-product/', product_create_view, name='create_product'),
    path('update-product/<int:id>/', product_create_update_view, name='update_product'),
    path('delete-product/<int:id>/', product_delete_view, name='delete_product'),
]
