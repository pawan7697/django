from django.urls import path
from .import views


urlpatterns = [
    path('addproducts/', views.addproducts, name='addproducts'),
    path('productSubmit/', views.productSubmit, name='productSubmit'),
  
]