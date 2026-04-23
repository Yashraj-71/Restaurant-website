from django.db import models


class Inquiry(models.Model):
    class Service(models.TextChoices):
        SWEETS = "sweets", "Sweets order"
        ROOM = "room", "Room booking"

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


class Room(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    tag = models.CharField(max_length=50)  # e.g., Deluxe, Family, Executive
    description = models.TextField()
    price = models.CharField(max_length=50)
    image_name = models.CharField(
        max_length=100
    )  # e.g., room1.jpeg (assumed to be in static/website/img/)

    def __str__(self):
        return self.name
