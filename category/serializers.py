from rest_framework.serializers import ModelSerializer

from restaurant.models import Restaurant
from category.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", )

    def create(self, validated_data):
        restaurant = Restaurant.objects.get(administrator=self.context['request'].user)

        data = validated_data.copy()
        data['restaurant'] = restaurant

        return super().create(data)
