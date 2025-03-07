from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    product_data = []

    for product in products:
        product_data.append({
            "id": product.uuid,
            "name": product.name,
            "brand": product.brand,
            "category": product.category,
            "description": product.description,
            "rating": product.rating,
            "numReviews": product.numReviews,
            "price": product.price,
            "stock": product.stock,
            "createdAt": product.createdAt,
            "updatedAt": product.updatedAt,
            "image": product.image.url if product.image else None,
        })

    return Response(product_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, product_uuid):
    product = get_object_or_404(Product, uuid=product_uuid) 

    product_data = {
        "id": product.uuid,
        "name": product.name,
        "brand": product.brand,
        "category": product.category,
        "description": product.description,
        "rating": product.rating,
        "numReviews": product.numReviews,
        "price": product.price,
        "stock": product.stock,
        "createdAt": product.createdAt,
        "updatedAt": product.updatedAt,
        "image": product.image.url if product.image else None,
    }

    return Response(product_data, status=status.HTTP_200_OK)
