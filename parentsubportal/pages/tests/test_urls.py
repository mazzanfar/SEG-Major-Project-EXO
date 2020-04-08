from django.test import SimpleTestCase
from django.urls import home_page, blogs_page
from pages.views import home_page, blogs_page

class TestUrls(SimpleTestCase):
    def test_homePage_url_is_resolved(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func, 'home_page')

    def test_blogsPage_url_is_resolved(self):
        url = reverse('blogs_page')
        self.assertEquals(resolve(url).func, 'blog_page')
