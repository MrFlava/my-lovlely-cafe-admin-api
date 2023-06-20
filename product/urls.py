from django.urls import path

from product.views import ProductCreateView, ProductListView, ProductRetrieveView, ProductUpdateView, ProductDestroyView


app_name = "category"

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create-product'),
    path('list/<int:restaurant_id>/', ProductListView.as_view(), name='list-product'),
    path('<int:id>/info/', ProductRetrieveView.as_view(), name='product-info'),
    path('<int:id>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:id>/delete/', ProductDestroyView.as_view(), name='product-destroy'),
]
