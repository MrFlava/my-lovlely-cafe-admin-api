from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth_app.authentication import TokenAuthentication
from category.serializers import CategorySerializer
from category.models import Category
from restaurant.models import Restaurant


class CategoryCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer


class CategoryListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        restaurant = Restaurant.objects.get(administrator=self.request.user)

        return Category.objects.filter(restaurant=restaurant)


class CategoryRetrieveView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        category_info = get_object_or_404(Category, pk=kwargs["id"])

        serializer = self.get_serializer(category_info)
        return Response(serializer.data)


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer
    lookup_field = "id"


class CategoryDestroyView(DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = CategorySerializer
    lookup_field = "id"
