from django.test import TestCase
from django.urls import reverse

from .models import Inquiry


class HomePageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rv sweets and restaurant")

    def test_inquiry_form_saves_submission(self):
        response = self.client.post(
            reverse("home"),
            {
                "name": "Aarav",
                "phone": "9876543210",
                "email": "aarav@example.com",
                "service": Inquiry.Service.CATERING,
                "message": "Need catering for 200 guests.",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Inquiry.objects.count(), 1)
        self.assertContains(response, "Our team will contact you shortly")
