from django.urls import path
from .import views

urlpatterns = [
path('addSupercateory/', views.addSupercateory, name='addSupercateory'),
path('ajaxsubcategory/', views.ajaxsubcategory, name='ajaxsubcategory'),
path('SupercategorySubmit/', views.SupercategorySubmit, name='SupercategorySubmit'),
path('SupercategoryView/', views.SupercategoryView, name='SupercategoryView'),

]