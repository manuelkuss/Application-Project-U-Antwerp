from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


# Create your tests here.

class NoteAPITests(APITestCase):
    def test_get_notes_status(self):
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_notes(self):
        # Get the API endpoint using DRF's router name (e.g. 'note-list')
        response = self.client.get(reverse('note-list'))

        # Ensure the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Convert JSON response to Python list
        data = response.json()

        # Check that at least one note is returned
        self.assertTrue(len(data) > 0, "Expected at least one note in the response")
