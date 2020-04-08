from django.test import TestCase, Client
from django.urls import reverse
from django.models import Timeline, Pdf

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.timeline_url = reverse('timeline')
        self.upload_url = reverse('upload')

    def test_timeline_GET(self):
        response = self.client.get(self.timeline_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'timeline.html')

    def test_upload_POST(self):
        response = self.client.post(self.upload_url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'upload.html')
