from dataclasses import dataclass

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status
#tests based on improvement branch version
@dataclass
class InvalidCredentialCase:
    name: str
    data: dict

class LoginTestCase(TestCase):
    URL_LOGIN = reverse_lazy('login')
    URL_PROFILE = reverse_lazy('profile')

    VALID_USER_USERNAME = 'testuser'
    VALID_USER_PASSWORD = 'testpassword'

    INACTIVE_USER_USERNAME = 'testuserinactive'
    INACTIVE_USER_PASSWORD = 'testpasswordinactive'

    INVALID_CREDENTIAL_CASES = [
        InvalidCredentialCase(
            name='wrong-password',
            data={
                'username': VALID_USER_USERNAME,
                'password': 'wrong',
            },
        ),
        InvalidCredentialCase(
            name='wrong-username-and-password',
            data={
                'username': 'wrong',
                'password': 'wrong'
            },
        ),
        InvalidCredentialCase(
            name='inactive-user',
            data={
                'username': INACTIVE_USER_USERNAME,
                'password': INACTIVE_USER_PASSWORD,
            },
        ),
    ]

    def setUp(self):
        self.valid_user = get_user_model().objects.create_user(
            username=self.VALID_USER_USERNAME,
            password=self.VALID_USER_PASSWORD,
            is_active=True,
        )
        self.inactive_account = get_user_model().objects.create_user(
            username=self.INACTIVE_USER_USERNAME,
            password=self.INACTIVE_USER_PASSWORD,
            is_active=False,
        )

    def test_url_works(self):
        response = self.client.get(path=self.URL_LOGIN)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_valid_account(self):
        response = self.client.post(
            path=self.URL_LOGIN,
            data={
                'username': self.VALID_USER_USERNAME,
                'password': self.VALID_USER_PASSWORD
            },
            follow=True,
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.valid_user, response.context['user'])
        self.assertRedirects(
            response,
            self.URL_PROFILE,
            status_code=status.HTTP_302_FOUND
        )        

    def test_invalid_credentials(self):
        for case in self.INVALID_CREDENTIAL_CASES:
            with self.subTest(name=case.name):
                response = self.client.post(
                    path=self.URL_LOGIN,
                    data=case.data
                )
                self.assertEqual(status.HTTP_200_OK, response.status_code)
                self.assertEqual(
                    {
                        '__all__': [
                            'Please enter a correct username and password. '
                            'Note that both fields may be case-sensitive.'
                        ]
                    },
                    response.context['form'].errors,
                )

class LogoutTestCase(TestCase):
    URL_LOGOUT = reverse_lazy('logout')

    def setUp(self):
        self.valid_user = get_user_model().objects.create_user(
            username='testuser',
            password='irrelevant',
            is_active=True,
        )

    def test_authorized_user(self):
        self.client.force_login(self.valid_user)
        response = self.client.get(self.URL_LOGOUT)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'users/logout.html')
        self.assertIsInstance(response.context['user'], AnonymousUser) 

    def test_unauthorized_user(self): 
        self.client.logout()
        response = self.client.get(self.URL_LOGOUT)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'users/logout.html')
        self.assertIsInstance(response.context['user'], AnonymousUser)                      