from posts.models import Post
import pytest

@pytest.mark.django_db
class TestModels:

    def test_negative_post_below_min_votes(self):
