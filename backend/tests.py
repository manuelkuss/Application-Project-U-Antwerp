from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Note, MgfFile


class NoteModelTests(TestCase):
    def setUp(self):
        Note.objects.create(title="Note 1", content="This is note one")
        Note.objects.create(title="Note 2", content="This is note two")

    def test_fetching_notes(self):
        note = Note.objects.get(title="Note 1")
        self.assertEqual(note.content, "This is note one")

    def test_adding_notes(self):
        numberOfNotesBeforeInsertion = len(Note.objects.all())
        self.assertEqual(numberOfNotesBeforeInsertion, 2)

        Note.objects.create(title="Note 3", content="This is note three")

        numberOfNotesAfterInsertion = len(Note.objects.all())
        self.assertEqual(numberOfNotesAfterInsertion, 3)


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
        self.assertEqual(len(data), 2, "Expected exactly two notes in the response")

    def test_add_note_via_post_request(self):
        new_note = {
            "title": "New note titel",
            "content": "New note content"
        }
        response1 = self.client.post(reverse('note-list'), data=new_note, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)

        response2 = self.client.get(reverse('note-list'))
        self.assertEqual(len(response2.json()), 3, "Expected exactly three notes")


class MgfFileAPITests(APITestCase):
    def setUp(self):
        # Create multiple notes for testing
        MgfFile.objects.create(name="Test file 1")
        MgfFile.objects.create(name="Test file 2")

    def test_get_mgf_files(self):
        response = self.client.get(reverse('mgffile-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2, "Expected two mgf files in the response")
        self.assertEqual(data[0].get("name"), "Test file 1")


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

