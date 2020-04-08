from django.test import TestCase
from disability.models import Keyword, Disability, PDFFile


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Keyword.objects.create(title = 'cancer')
        Disability.objects.create(title = 'cancer')

    def test_variable_name_label(self):
        Keyword = Keyword.objects.get(id=1)
        field_label = Keyword._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

        Disability = Disability.objects.get(id=1)
        field_label = Disability._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_variable_max_length(self):
        Keyword = Keyword.objects.get(id=1)
        max_length = Keyword._meta.get_field('title').max_length
        self.assertEquals(max_length, 120)

        Disability = Disability.objects.get(id=1)
        max_length = Keyword._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)
