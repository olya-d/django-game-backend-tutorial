from rest_framework import serializers

from .models import Item, Inventory


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
