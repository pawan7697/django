from django.urls import path
from .import views

urlpatterns = [
    path('addSubcategory/', views.addSubcategory, name='addSubcategory'),
    path('submitSubcategory/', views.submitSubcategory, name='submitSubcategory'),
    path('subcategoryView/', views.subcategoryView, name='subcategoryView'),
    path('subcategoryEdit/<int:ids>', views.subcategoryEdit, name='subcategoryEdit'),
    path('subcategoryUpadte/', views.subcategoryUpadte, name='subcategoryUpadte'),
    
    
]