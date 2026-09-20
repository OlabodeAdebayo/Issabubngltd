from rest_framework.test import APITestCase
from projects.models import Project

class ProjectApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(title='Test Project',slug='test-project',category='commercial',description='A test project.')

    def test_project_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_category_filter(self):
        response = self.client.get('/api/projects/?category=commercial')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
