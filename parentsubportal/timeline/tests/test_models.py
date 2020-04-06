from django.test import TestCase
from Timeline.views import Timeline, Pdf
from children.models import Children

class testModels(TestCase):
    def setUp(self):
        self.timeline1 = Timeline.objects.create(
            header = 'Financial Support',
            age = '0-4',
            child = Children.objects.create(
                firstname = 'hedi',
                lastname = 'gha',
                age = '3',
                disability = 'lagging'
            )
        )

    def test_timeline_created(self):
        self.assertEquals(self.timeline1.header, 'Financial Support')
        self.assertEquals(self.timeline1.child.age, '3')
