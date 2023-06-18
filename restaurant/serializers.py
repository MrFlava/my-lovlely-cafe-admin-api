from rest_framework.serializers import ModelSerializer

from restaurant.models import Restaurant


class RestaurantSerializer(ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ("name", "address", "weekday", "from_hour", "to_hour", )

    def create(self, validated_data):
        data = validated_data.copy()
        data['administrator'] = self.context['request'].user

        return super().create(data)


class RestaurantUpdateSerializer(ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ("name", "address", "weekday", "from_hour", "to_hour",)
        read_only_fields = ("administrator", )
