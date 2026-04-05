from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="icecream", price=80,inventory=100)
        self.assertEqual(str(item), "icecream : 80")