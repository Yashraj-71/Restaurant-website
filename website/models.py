from django.db import models


class Inquiry(models.Model):
    class Service(models.TextChoices):
        SWEETS = "sweets", "Sweets order"
        DINING = "dining", "Restaurant booking"
        CATERING = "catering", "Event catering"
        BULK = "bulk", "Bulk corporate order"

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    service = models.CharField(
        max_length=20,
        choices=Service.choices,
        default=Service.SWEETS,
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.get_service_display()}"
