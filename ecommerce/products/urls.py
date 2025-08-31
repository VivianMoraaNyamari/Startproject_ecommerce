from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('', views.ProductList.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('<int:product_id>/reviews/', views.ProductReviewList.as_view(), name='product-review-list'),
    path('reviews/<int:pk>/', views.ProductReviewDetail.as_view(), name='product-review-detail'),
]
