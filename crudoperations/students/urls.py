from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
   
    path('', views.index , name="home"),
    path('delete/<int:id>', views.delete_data , name="deletedata"),
    path('edit/<int:id>', views.edit_data , name="editdata"),
    path('search/', views.search_data , name="searchdata"),
]