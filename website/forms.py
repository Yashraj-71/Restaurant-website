from django import forms

from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["name", "phone", "email", "service", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Your name", "autocomplete": "name"}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "Phone number", "autocomplete": "tel"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Email address", "autocomplete": "email"}
            ),
            "service": forms.Select(),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Tell us about your order, catering, or table booking",
                    "rows": 4,
                }
            ),
        }
