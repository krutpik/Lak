from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu'),
    path('<int:topic_id>/', views.description, name='description'),
    path('new_description/<int:topic_id>/', views.new_description, name='new_description'),
    path('delete/<int:description_id>/', views.delete_description, name='delete_description'),
    path('edit_description/<int:entry_id>/', views.edit_description, name='edit_entry'),
]

