from django.urls import path
from .import views

urlpatterns = [
    path('categorys/', views.categorys, name='categorys'),
    path('submitcategory/', views.submitcategory, name='submitcategory'),
    path('categoryView/', views.categoryView, name='categoryView'),
    path('categoryEdit/<int:ids>', views.categoryEdit, name='categoryEdit'),
    path('categoryUpdate/', views.categoryUpdate, name='categoryUpdate'),
    
]