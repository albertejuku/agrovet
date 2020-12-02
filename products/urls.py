from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('newitem/', views.ProductCreate.as_view(), name='new_item'),
    path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('product/<pk>/update', views.UpdateProduct.as_view(), name='update'),
     path('product/<pk>/delete', views.Delete.as_view(), name='delete')
]