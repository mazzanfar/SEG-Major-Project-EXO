from django.test import SimpleTestCase
from django.urls import reverse, resolve
from timeline.views import timeline, upload

class TestUrls(SimpleTestCase):
    def test_timeline_url(self):
        url = reverse('timeline')
        self.assertEquals(resolve(url).func, timeline)

    def test_upload_url(self):
        url = reverse('upload')
        self.assertEquals(resolve(url).func, upload)
