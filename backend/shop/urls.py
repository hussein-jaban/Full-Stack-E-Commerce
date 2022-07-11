from django.urls import path
from backend.shop.views import *

urlpatterns = [
    path('categories/', get_categories),
    path('category/<pk>/', single_category),
    path('products/', get_products),
    path('product/<pk>/', single_product),
    path('post/product/', post_product),
    path('user/products/<pk>/', get_user_products),
    path('certain_category/<pk>/', certain_category),
    path('similar_items/<pk>/', similar_items),
    path('product/<pk>/reviews/', get_reviews),

    path('xproducts/', ProductListView.as_view()),
    path('xproduct/<slug>/', ProductDetailView.as_view()),
    path('xproduct/<slug>/reviews/', ReviewListView.as_view()),
]
