from django.urls import path
from .views import scrape_webpage

app_name = 'crawler'

crawler_urls = [
    path('', scrape_webpage, name='crawl'),
]