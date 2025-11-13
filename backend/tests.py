from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Note

class NoteModelTests(TestCase):
    def setUp(self):
        Note.objects.create(title="Note 1", content="This is note one")
        Note.objects.create(title="Note 2", content="This is note two")

    def test_notes(self):
        note = Note.objects.get(title="Note 1")
        self.assertEqual(note.content, "This is note one")

class NoteAPITests(APITestCase):

    def setUp(self):
        # Create multiple notes for testing
        Note.objects.create(title="Note 1", content="This is note one")
        Note.objects.create(title="Note 2", content="This is note two")

    def test_get_notes(self):
        response = self.client.get(reverse('note-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 1, "Expected more than one note in the response")


class ChartDataAPITests(APITestCase):

    def test_get_chart_data(self):

        url = reverse('chart-data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that response data is a list
        self.assertIsInstance(response.data, list)

        # Check that exactly 3 chart spectra are returned
        self.assertEqual(len(response.data), 3)

        chart_data = response.data[0]
        self.assertIn('mz', chart_data)
        self.assertIn('intensity', chart_data)
