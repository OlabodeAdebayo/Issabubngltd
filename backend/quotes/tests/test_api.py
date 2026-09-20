from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class QuoteApiTests(APITestCase):
    def test_health_endpoint(self):
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')

    def test_quote_create(self):
        payload = {
            'full_name':'Test Client','email':'client@example.com','phone':'+2348000000000',
            'service':'Building & Construction','project_location':'Ota, Ogun State',
            'message':'We need a quotation for a proposed building project.'
        }
        response = self.client.post('/api/quotes/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'new')
