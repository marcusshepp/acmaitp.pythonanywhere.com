from datetime import datetime

from django.test import TestCase

from .models import Update


class SimpleTest(TestCase):

    def test_create_update(self):
        obj = {
            "when": datetime.now(),
            "where": "Pearce 323",
            "what": "Programming",
        }
        update = Update.objects.get_or_create(**obj)
        boolean = Update.objects.filter(**obj).exists()
        self.assertTrue(boolean)
