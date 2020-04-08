from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.homePage_url = reverse('home_page')
        self.blogsPage_url = reverse('blogs_page')

    def test_homePage_GET(self):
        response = self.client.get(self.homePage_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home_page.html')


    def test_blogsPage_GET(self):
        response = self.client.get(self.blogsPage_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/blogs_page.html')
