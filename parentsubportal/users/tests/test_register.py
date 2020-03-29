from dataclasses import dataclass

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status

#tests based on improvement branch version
@dataclass
class InvalidDataCase:
    name: str
    data: dict
    errors: dict

class RegisterTestCase(TestCase):
    URL_REGISTER = reverse_lazy('register')
    URL_LOGIN = reverse_lazy('login')

    EXISTING_DATA = {
        'email': 'user2@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'username': 'existinguser',
        'password1': 'ExampleSup3rStr0ngPassw0rd!',
        'password2': 'ExampleSup3rStr0ngPassw0rd!'
    }

    VALID_DATA = {
        'email': 'user@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'username': 'testuser',
        'password1': 'ExampleSup3rStr0ngPassw0rd!',
        'password2': 'ExampleSup3rStr0ngPassw0rd!'
    }

    INVALID_DATA = [
        InvalidDataCase(
            name='empty-form',
            data={},
            errors={
                'email': ['This field is required.'],
                'username': ['This field is required.'],
                'password1': ['This field is required.'],
                'password2': ['This field is required.'],
            },
        ),
        InvalidDataCase(
            name='invalid-email',
            data={
                'email': 'xxxx',
                'username': 'testinvalid1',
                'password1': 'TestPassw0rd1!',
                'password2': 'TestPassw0rd1!',
            },
            errors={
                'email': ['Enter a valid email address.'],
            },
        ),
        InvalidDataCase(
            name='existing-account',
            data={
                'email': 'johndoe@example.com',
                'username': EXISTING_DATA['username'],
                'password1': 'TestPassw0rd1!',
                'password2': 'TestPassw0rd1!',
            },
            errors={
                'username': ['A user with that username already exists.'],
            },
        ),
        InvalidDataCase(
            name='weak-password',
            data={
                'email': 'johndoe@example.com',
                'username': 'testinvalid2',
                'password1': '123',
                'password2': '123',
            },
            errors={
                'password2': [
                    'This password is too short. '
                    'It must contain at least 8 characters.',
                    'This password is too common.',
                    'This password is entirely numeric.',
                ],
            },
        ),
    ]

    def setUp(self):
        get_user_model().objects.create_user(
            username=self.EXISTING_DATA['username'],
            first_name=self.EXISTING_DATA['first_name'],
            last_name=self.EXISTING_DATA['last_name'],
            email=self.EXISTING_DATA['email'],
        )

    def test_get(self):
        response = self.client.get(self.URL_REGISTER)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_valid_data(self):
        response = self.client.post(
            path=self.URL_REGISTER,
            data=self.VALID_DATA,
            follow=True
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertRedirects(response, self.URL_LOGIN)
        self.assertEqual(
            'Your account has been created. Your are now able to login!',
            str(list(response.context['messages'])[0]),
        )
        user = get_user_model().objects.filter(
            username=self.VALID_DATA['username'],
            first_name=self.VALID_DATA['first_name'],
            last_name=self.VALID_DATA['last_name'],
            email=self.VALID_DATA['email'],
        ).first()
        self.assertIsNotNone(
            user, msg='User has not been created in the database'
        )
        self.assertTrue(
            user.check_password(self.VALID_DATA['password1']),
            msg=(
                'The password used in form is not the one saved in the '
                'database'
            )
        )

    def test_invalid_data(self):
        for case in self.INVALID_DATA:
            with self.subTest(name=case.name):
                response = self.client.post(
                    path=self.URL_REGISTER,
                    data=case.data,
                )
                self.assertEqual(status.HTTP_200_OK, response.status_code)
                username = case.data.get('username')
                if username and username != self.EXISTING_DATA['username']:
                    self.assertFalse(
                        get_user_model().objects.filter(
                            username=username
                        ).exists(),
                        msg='User has been created, but should not have been'
                    )
                self.assertDictEqual(
                    case.errors, response.context['form'].errors
                )                