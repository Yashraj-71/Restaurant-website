from django.contrib import admin

from .models import Inquiry, Room


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "service", "phone", "email", "created_at")
    list_filter = ("service", "created_at")
    search_fields = ("name", "phone", "email", "message")
    readonly_fields = ("created_at",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "tag", "price")
    prepopulated_fields = {"slug": ("name",)}
