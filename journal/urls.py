from django.contrib import admin
from django.urls import path
from journal.views import home, add_resource, delete_resource, profile

app_name = 'journal'

urlpatterns = [
    path('', home, name='home'),
    path('new_resource', add_resource, name='new_resource'),
    path('delete_resource', delete_resource, name='delete_resource'),
    path('profile', profile, name='profile'),
    path('new_resource/<int:resource_id>/', add_resource, name='new_resource'),
    path('delete_resource/<int:resource_id>/', delete_resource, name='delete_resource'),
    path('profile', profile, name='profile'),

]

