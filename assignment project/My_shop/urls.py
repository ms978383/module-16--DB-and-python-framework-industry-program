from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.sign_up,name='register'),
    path('',views.login,name='login'),
    path('Add-products',views.add_products,name='Add-products'),
    path('All-products',views.all_products,name="All-products"),
    path('Logout/',views.logout,name="Logout"),
    path('edit/<int:id>/',views.edit_products,name="edit-products"),
    path('update/<int:id>/',views.update_products,name="update-products"),
    path('delete/<int:id>/',views.delete_products,name="delete")
    
    
]