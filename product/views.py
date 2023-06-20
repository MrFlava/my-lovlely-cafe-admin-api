from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auth_app.authentication import TokenAuthentication
from product.serializers import ProductSerializer
from product.models import Product


class ProductCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProductSerializer


class ProductRetrieveView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        product_info = get_object_or_404(Product, pk=kwargs["id"])

        serializer = self.get_serializer(product_info)
        return Response(serializer.data)


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProductSerializer
    lookup_field = "id"


class ProductDestroyView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProductSerializer
    lookup_field = "id"