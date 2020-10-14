from django.urls import path
from product import views

urlpatterns = [
    path('product_home/', views.ProductListView.as_view(), name='product_home'),
    path('product_home/<int:pk>', views.ProductDetailView.as_view(), name='product_home_item'),
]



