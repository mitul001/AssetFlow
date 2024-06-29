from django.urls import path
from . import views

urlpatterns = [
    path('create-contact/',views.contact_create_view,name='create_contact'),
    path('list-contact/',views.contact_list_view,name='list_contact'),
]
