from django.db.utils import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from restaurant.serializers import RestaurantSerializer, RestaurantUpdateSerializer
from restaurant.mixins import RestaurantMixin
from restaurant.models import Restaurant
from auth_app.authentication import TokenAuthentication


class RestaurantCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    serializer_class = RestaurantSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": "Integrity Error! This administrator has restaurant already"},
                status=status.HTTP_400_BAD_REQUEST
            )


class RestaurantRetrieveView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = RestaurantSerializer

    def retrieve(self, request, *args, **kwargs):
        restaurant_info = Restaurant.objects.get(administrator=request.user)

        serializer = self.get_serializer(restaurant_info)
        return Response(serializer.data)


class RestaurantUpdateView(RestaurantMixin, UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)
    serializer_class = RestaurantUpdateSerializer
    lookup_field = 'pk'
