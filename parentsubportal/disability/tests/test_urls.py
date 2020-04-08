from django.test import SimpleTestCase
from django.urls import search, search_results
from disability.views import HomePageView, SearchResultsView

class TestUrls(SimpleTestCase):
    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, 'HomePageView')

    def test_blogsPage_url_is_resolved(self):
        url = reverse('search_results')
        self.assertEquals(resolve(url).func, 'SearchResultsView')
