from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products, name='get_products'),
    path('products/<uuid:product_uuid>/', views.get_product, name='get_product'),
]
