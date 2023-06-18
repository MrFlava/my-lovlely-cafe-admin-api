from django.shortcuts import get_object_or_404

from restaurant.models import Restaurant


class RestaurantMixin(object):
    queryset = Restaurant.objects.all()
    lookup_field = None

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        try:
            obj = get_object_or_404(queryset, administrator=self.request.user)
            self.check_object_permissions(self.request, obj)
            return obj
        except Exception:
            pass

