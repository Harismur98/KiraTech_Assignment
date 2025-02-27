from rest_framework import serializers
from .models import Inventory, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name']

class InventorySerializer(serializers.ModelSerializer):
    supplier = serializers.StringRelatedField() 

    class Meta:
        model = Inventory
        fields = ['id', 'name', 'supplier', 'availability'] 