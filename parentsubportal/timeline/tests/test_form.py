from django.test import SimpleTestCase
from Timeline.forms import TimelineForm, PdfForm

class TextForms(SimpleTestCase):
    def test_TimelineForm_valid_data(self):
        form = TimelineForm(data={
            'header': 'Educational Support'
            'age': '4'
            'child': 'hedi'
        })
        self.assertTrue(form.is_valid())

    def test_TimelineForm_no_data(self):
        form = TimelineForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
