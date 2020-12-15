from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

class SignupTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_signup(self):
        response = self.c.post('user/signup',
                          {  'username': 'john',
                             'password': 'smith'})
        self.assertNotEqual(
            User.objects.filter(
                username='john'
            ),
            []
        )
                              