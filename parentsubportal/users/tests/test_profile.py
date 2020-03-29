from dataclasses import dataclass
from urllib.parse import urlencode

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status

#tests based on improvement branch version

@dataclass
class InvalidDataCase:
    name: str
    data: dict
    p_form_errors: dict
    u_form_errors: dict

class ProfileTestCase(TestCase):
    URL_PROFILE = reverse_lazy('profile')
    URL_LOGIN = reverse_lazy('login')

    VALID_USER_DATA = {
        'email': 'newemail@example.com',
        'first_name': 'NewJohn',
        'last_name': 'NewDoe',
        'username': 'newusername',
    }
    VALID_PROFILE_DATA = {
        'image': SimpleUploadedFile(
            name='example.jpg',
            content=EXAMPLE_IMAGE,
            content_type='image/jpeg'
        )
    }

    INVALID_DATA_CASES = [
        InvalidDataCase(
            name='empty-forms',
            data={},
            p_form_errors={},
            u_form_errors={
                'username': ['This field is required.'],
                'email': ['This field is required.']
            }
        ),
        InvalidDataCase(
            name='invalid-email',
            data={
                'username': 'newusername',
                'email': 'invalidemail'
            },
            p_form_errors={},
            u_form_errors={
                'email': ['Enter a valid email address.'],
            }
        ),
    ]

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
        )

    def test_unauthorized(self):
        for method in ['GET', 'POST', 'HEAD', 'DELETE']:
            with self.subTest(name=method):
                self.client.logout()
                response = getattr(self.client, method.lower())(
                    self.URL_PROFILE,
                    follow=True
                )
                self.assertEqual(status.HTTP_200_OK, response.status_code)
                qp = urlencode({'next': self.URL_PROFILE})
                self.assertRedirects(response, f'{self.URL_LOGIN}?{qp}')

    def test_get_authorized(self):
        self.client.force_login(self.user)
        response = self.client.get(self.URL_PROFILE)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_valid_data(self):
        data = {}
        data.update(self.VALID_USER_DATA)
        data.update(self.VALID_PROFILE_DATA)
        self.client.force_login(self.user)
        response = self.client.post(
            path=self.URL_PROFILE,
            data=data,
            follow=True,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertRedirects(response, self.URL_PROFILE)

        self.user.refresh_from_db()
        self.assertEqual(self.VALID_USER_DATA['username'], self.user.username)
        self.assertEqual(self.VALID_USER_DATA['email'], self.user.email)
        self.assertEqual(self.VALID_USER_DATA['first_name'],
                         self.user.first_name)
        self.assertEqual(self.VALID_USER_DATA['last_name'],
                         self.user.last_name)

    def test_invalid_data(self):
        self.client.force_login(self.user)
        for case in self.INVALID_DATA_CASES:
            with self.subTest(name=case.name):
                response = self.client.post(
                    path=self.URL_PROFILE,
                    data=case.data,
                    follow=True,
                )
                self.assertEqual(status.HTTP_200_OK, response.status_code)
                self.assertEqual(
                    case.p_form_errors,
                    response.context['p_form'].errors
                )
                self.assertEqual(
                    case.u_form_errors,
                    response.context['u_form'].errors
                )        