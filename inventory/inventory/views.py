from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Inventory, Supplier
from .serializers import InventorySerializer

class InventoryListAPI(generics.ListAPIView):
    serializer_class = InventorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return Inventory.objects.select_related('supplier').all()

def inventory_page(request):
    return render(request, 'inventory/inventory_list.html')

def inventory_detail_page(request, id):
    item = get_object_or_404(Inventory, id=id)
    return render(request, 'inventory/inventory_detail.html', {'item': item}) 