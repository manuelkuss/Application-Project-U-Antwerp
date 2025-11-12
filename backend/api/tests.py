from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


# Create your tests here.

class NoteAPITests(APITestCase):
    def test_get_notes(self):
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

