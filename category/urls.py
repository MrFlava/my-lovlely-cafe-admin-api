from django.urls import path

from category.views import (
    CategoryCreateView,
    CategoryListView,
    CategoryRetrieveView,
    CategoryUpdateView,
    CategoryDestroyView
)


app_name = "category"

urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name='create-category'),
    path('list/', CategoryListView.as_view(), name='list-category'),
    path('<int:id>/info/', CategoryRetrieveView.as_view(), name='category-info'),
    path('<int:id>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('<int:id>/delete/', CategoryDestroyView.as_view(), name='category-destroy'),
]
