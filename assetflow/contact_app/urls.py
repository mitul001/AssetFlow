from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.contact_create_view,name='create_contact'),
    path('list/',views.contact_list_view,name='contact_list'),
]
