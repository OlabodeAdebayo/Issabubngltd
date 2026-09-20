from rest_framework.test import APITestCase
from services.models import Service

class ServiceApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Service.objects.create(number='01',title='Test Service',slug='test-service',description='A test service.',active=True)

    def test_active_service_list(self):
        response = self.client.get('/api/services/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
