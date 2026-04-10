from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings


from .forms import InquiryForm


def home(request):
    menu_sections = [
        {
            "title": "Sweets",
            "items": [
            {"name": "Kaju Katli", "price": "₹900/kg"},
            {"name": "Gulab Jamun", "price": "₹25/pc"},
            {"name": "Rasgulla", "price": "₹25/pc"},
            {"name": "Rasmalai", "price": "₹50/pc"},
            {"name": "Milk Cake", "price": "₹450/kg"},
            {"name": "Motichoor Laddu", "price": "₹500/kg"},
            {"name": "Besan Laddu", "price": "₹400/kg"},
            {"name": "Peda", "price": "₹420/kg"},
            {"name": "Soan Papdi", "price": "₹300/kg"},
            {"name": "Kalakand", "price": "₹480/kg"},
            {"name": "Mysore Pak", "price": "₹520/kg"},
            {"name": "Balushahi", "price": "₹380/kg"},
            {"name": "Jalebi", "price": "₹300/kg"},
            {"name": "Rabri", "price": "₹60/bowl"},
            {"name": "Cham Cham", "price": "₹40/pc"},
            {"name": "Coconut Barfi", "price": "₹450/kg"},
            {"name": "Dry Fruit Roll", "price": "₹1100/kg"},
            {"name": "Anjeer Barfi", "price": "₹1200/kg"},
    ],
        },
        {
            "title": "Restaurant",
            "items": [
    {"name": "Water Bottle", "price": "MRP"},
    {"name": "Spe Tea", "price": "₹30"},
    {"name": "Coffee", "price": "₹40"},
    {"name": "Hot Milk", "price": "₹40"},
    {"name": "Cold Drink", "price": "MRP"},

    {"name": "Paneer Tikka Dry", "price": "₹350"},

    {"name": "Pyaj Salad", "price": "₹40"},
    {"name": "Tomato Salad", "price": "₹60"},
    {"name": "Green Salad", "price": "₹80"},
    {"name": "Cucumber Salad", "price": "₹60"},

    {"name": "Rosted Papad", "price": "₹20"},
    {"name": "Masala Papad", "price": "₹40"},
    {"name": "Fry Papad", "price": "₹40"},
    {"name": "Fry Masala Papad", "price": "₹60"},

    {"name": "Sada Dahi", "price": "₹50"},
    {"name": "Plain Raita", "price": "₹70"},
    {"name": "Veg Raita", "price": "₹80"},
    {"name": "Boondi Raita", "price": "₹80"},

    {"name": "Plain Rice", "price": "₹90"},
    {"name": "Jeera Rice", "price": "₹100"},
    {"name": "Lemon Rice", "price": "₹120"},
    {"name": "Mattar Pulav", "price": "₹130"},
    {"name": "Veg Pulav", "price": "₹150"},
    {"name": "Hyderabadi Biryani", "price": "₹180"},
    {"name": "Veg Biryani", "price": "₹180"},

    {"name": "Namkeen Chach", "price": "₹30"},
    {"name": "Namkeen Lassi", "price": "₹60"},
    {"name": "Mithi Lassi", "price": "₹50"},

    {"name": "Matar Paneer", "price": "₹200"},
    {"name": "Palak Paneer", "price": "₹220"},
    {"name": "Shahi Paneer", "price": "₹220"},
    {"name": "Paneer Do Pyaza", "price": "₹230"},
    {"name": "Kadai Paneer", "price": "₹230"},
    {"name": "Handi Paneer", "price": "₹250"},
    {"name": "Kadai Paneer (Special)", "price": "₹260"},
    {"name": "Paneer Lababdar", "price": "₹240"},
    {"name": "Paneer Butter Masala", "price": "₹250"},
    {"name": "Kaaju Paneer Masala", "price": "₹300"},
    {"name": "Paneer Bhurji", "price": "₹300"},
    {"name": "Kaaju Kari", "price": "₹280"},
    {"name": "Mushroom Mattar", "price": "₹220"},
    {"name": "Mushroom Masala", "price": "₹250"},
    {"name": "Kadai Mushroom", "price": "₹230"},
    {"name": "Paneer Kolhapuri", "price": "₹250"},
    {"name": "Paneer Toofani", "price": "₹240"},
    {"name": "Veg Jaipuri", "price": "₹200"},
    {"name": "Methi Malai Matar", "price": "₹200"},
    {"name": "Malai Kofta", "price": "₹250"},
    {"name": "Paneer Amritsari", "price": "₹260"},
    {"name": "Paneer Tikka Masala Gravy", "price": "₹350"},
    {"name": "RV Special Sabji", "price": "₹350"},

    {"name": "Aalu Pyaz", "price": "₹150"},
    {"name": "Aalu Gobhi", "price": "₹170"},
    {"name": "Aalu Chola", "price": "₹180"},
    {"name": "Aalu Palak", "price": "₹160"},
    {"name": "Jeera Aalu", "price": "₹150"},
    {"name": "Dam Aalu", "price": "₹180"},
    {"name": "Sev Tamatar", "price": "₹160"},
    {"name": "Sev Bhaji Milk", "price": "₹200"},
    {"name": "Gatta Masala", "price": "₹160"},
    {"name": "Chana Masala", "price": "₹160"},
    {"name": "Bhindi Masala", "price": "₹150"},

    {"name": "Dal Fry", "price": "₹140"},
    {"name": "Dal Tadka", "price": "₹160"},
    {"name": "Dal Makhni", "price": "₹180"},
    {"name": "Lahsun Chatni", "price": "₹100"},
    {"name": "Dahi Fry", "price": "₹100"},

    {"name": "Plain Tandoori Roti", "price": "₹15"},
    {"name": "Butter Tandoori Roti", "price": "₹20"},
    {"name": "Ajwain Roti", "price": "₹25"},
    {"name": "Missi Roti", "price": "₹40"},
    {"name": "Plain Naan", "price": "₹45"},
    {"name": "Butter Naan", "price": "₹55"},
    {"name": "Stuff Naan", "price": "₹90"},
    {"name": "Garlic Naan", "price": "₹80"},
    {"name": "Lachha Paratha", "price": "₹60"},

    {"name": "Tawa Plain Roti", "price": "₹10"},
    {"name": "Tawa Butter Roti", "price": "₹15"},
],
        },
        {
    "title": "Fast Food",
    "items": [
    {"name": "Special Chai", "price": "₹10"},
    {"name": "Kulhad Chai", "price": "₹20"},
    {"name": "Hot Coffee", "price": "₹25"},
    {"name": "Hot Milk", "price": "₹30"},
    {"name": "Meethi Lassi", "price": "₹40"},
    {"name": "Chhach", "price": "₹20"},

    {"name": "Samosa", "price": "₹20"},
    {"name": "Dal Kachori", "price": "₹20"},
    {"name": "Aloo Pyaz Kachori", "price": "₹25"},
    {"name": "Mirchi Bada", "price": "₹20"},
    {"name": "Bread Pakoda", "price": "₹25"},

    {"name": "Aloo Paratha", "price": "₹60"},
    {"name": "Aloo Pyaz Paratha", "price": "₹60"},
    {"name": "Mix Paratha", "price": "₹80"},
    {"name": "Paneer Paratha", "price": "₹100"},
    {"name": "Plain Paratha", "price": "₹40"},
    {"name": "Amul Butter (Extra)", "price": "₹10"},

    {"name": "Kadhi Chawal", "price": "₹70"},
    {"name": "Chola Chawal", "price": "₹80"},
    {"name": "Kadhi Chola Chawal", "price": "₹100"},

    {"name": "Chola Bhatura", "price": "₹80"},
    {"name": "Extra Bhatura", "price": "₹20"},
    {"name": "Pav Bhaji", "price": "₹60"},
    {"name": "Poha", "price": "₹40"},
    {"name": "Plain Maggi", "price": "₹50"},
    {"name": "Veg Masala Maggi", "price": "₹70"},
    {"name": "Veg Grill Sandwich", "price": "₹60"},
    {"name": "Veg Cheese Grill Sandwich", "price": "₹80"},
    {"name": "Veg Burger", "price": "₹40"},
    {"name": "Cheese Burger", "price": "₹60"},
    {"name": "Extra Pav", "price": "₹20"},

    {"name": "Plain Dosa", "price": "₹80"},
    {"name": "Masala Dosa", "price": "₹100"},
    {"name": "Paneer Dosa", "price": "₹140"},
    {"name": "Veg Uttapam", "price": "₹80"},
    {"name": "Onion Uttapam", "price": "₹70"},
    {"name": "Idli Sambar", "price": "₹50"},

    {"name": "Veg Chowmein", "price": "₹70"},
    {"name": "Chilli Paneer", "price": "₹180"},
    {"name": "Chilli Potato", "price": "₹140"},
    {"name": "Honey Chilli Potato", "price": "₹160"},
    {"name": "Chilli Soyabean", "price": "₹100"},
    {"name": "Crispy Veg", "price": "₹180"},
        ],
        },
    ]

    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save()

            # EMAIL CONTENT
            subject = "New Inquiry from Website"
        message = f"""
Name: {inquiry.name}
Phone: {inquiry.phone}
Email: {inquiry.email}
Service: {inquiry.service}
Message: {inquiry.message}
"""

        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['yashrajchandel090@gmail.com'],
                fail_silently=False,
            )
        except Exception as e:
            print("Email Error:", e)

        messages.success(request, "Inquiry sent successfully!")
        return redirect("home")
    else:
        form = InquiryForm()

    return render(
        request,
        "website/home.html",
        {"form": form, "menu_sections": menu_sections},
    )


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "website/signup.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("home")
