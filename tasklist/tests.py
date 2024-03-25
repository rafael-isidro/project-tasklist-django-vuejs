from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from tasklist.models import Tasklist

class TasklistAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_retrieve_tasklist(self):
        Tasklist.objects.create(title='Task 1', completed=False, user=self.user)
        Tasklist.objects.create(title='Task 2', completed=True, user=self.user)

        response = self.client.get('/list-create-tasklist/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_tasklist(self):
        data = {'title': 'New Task', 'completed': False, 'user': self.user.id}
        response = self.client.post('/list-create-tasklist/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tasklist.objects.count(), 1)
        self.assertEqual(Tasklist.objects.get().title, 'New Task')

    def test_update_tasklist(self):
        task = Tasklist.objects.create(title='Task 1', completed=False, user=self.user)
        updated_data = {'title': 'Updated Task', 'completed': True, 'user': self.user.id}
        response = self.client.put(f'/retrieve-update-destroy-tasklist/{task.id}/', updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Tasklist.objects.get().title, 'Updated Task')

    def test_delete_tasklist(self):
        task = Tasklist.objects.create(title='Task 1', completed=False, user=self.user)
        response = self.client.delete(f'/retrieve-update-destroy-tasklist/{task.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Tasklist.objects.count(), 0)
