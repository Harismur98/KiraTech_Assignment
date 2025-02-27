from django.test import TestCase, Client
from .models import Inventory, Supplier

class InventoryViewTests(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()
        
        # Create a sample inventory item for testing
        self.test_item = Inventory.objects.create(
            name="Test Item",
            stock=10,
            description="Test Description",
            note="Test Note",
            availability=True,
            supplier=Supplier.objects.create(name="Test Supplier")
        )

    def test_inventory_list_view(self):
        # Test the main inventory page
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)

    def test_inventory_api_view(self):
        # Test the API endpoint
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_view(self):
        # Test the detail view with the created test item
        response = self.client.get(f'/inventory/{self.test_item.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_view_invalid_id(self):
        # Test with an invalid ID (should return 404)
        response = self.client.get('/inventory/99999/')
        self.assertEqual(response.status_code, 404) 