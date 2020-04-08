from django.test import TestCase, Client
from django.urls import reverse, search, search_results

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.search_url = reverse('search')
        self.searchResults_url = reverse('search_results')

    def test_HomePageView_GET(self):
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'disability/homepage.html')


    def test_SearchResultsView_GET(self):
        response = self.client.get(self.searchResults_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'disability/search_results.html')
