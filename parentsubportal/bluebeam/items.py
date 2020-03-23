# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from metadata.models import FetchedData, BlogPost


class BluebeamItem(DjangoItem):
    # change with which model you want to use
    django_model = FetchedData
