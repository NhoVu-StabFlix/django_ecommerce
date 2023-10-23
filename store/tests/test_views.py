from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from store.models import Category, Product
from django.test import TestCase

from unittest import skip


@skip("demonstrating skipping")
class TestSkip(TestCase):

    def test_skip(self):
        pass
