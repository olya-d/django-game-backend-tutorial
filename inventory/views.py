from rest_framework import viewsets

from .models import Item, Inventory
from .serializers import ItemSerializer, InventorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('weight')
    serializer_class = ItemSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Inventory.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset
