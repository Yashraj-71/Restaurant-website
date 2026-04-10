from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import InquiryForm


def home(request):
    menu_sections = [
        {
            "title": "Sweets",
            "items": [
                {"name": "Kaju Katli", "description": "Classic cashew delight."},
                {"name": "Gulab Jamun", "description": "Soft balls in sugar syrup."},
                {"name": "Rasgulla", "description": "Spongy chenna sweet."},
                {"name": "Rasmalai", "description": "Saffron milk dumplings."},
                {"name": "Milk Cake", "description": "Rich caramelized milk sweet."},
                {"name": "Motichoor Laddu", "description": "Fine boondi laddus."},
                {"name": "Besan Laddu", "description": "Roasted gram flour laddus."},
                {"name": "Peda", "description": "Traditional milk peda."},
                {"name": "Soan Papdi", "description": "Flaky festive favorite."},
                {"name": "Kalakand", "description": "Soft grainy milk bar."},
                {"name": "Mysore Pak", "description": "Ghee-rich gram sweet."},
                {"name": "Balushahi", "description": "Layered glazed pastry sweet."},
                {"name": "Jalebi", "description": "Hot crisp sugar spirals."},
                {"name": "Rabri", "description": "Thick sweetened milk dessert."},
                {"name": "Cham Cham", "description": "Cream-filled chenna sweet."},
                {"name": "Coconut Barfi", "description": "Fresh coconut fudge."},
                {"name": "Dry Fruit Roll", "description": "Premium nut-filled roll."},
                {"name": "Anjeer Barfi", "description": "Fig and nut barfi."},
            ],
        },
        {
            "title": "Restaurant",
            "items": [
                {"name": "Royal Thali", "description": "Complete meal platter."},
                {"name": "Paneer Butter Masala", "description": "Creamy tomato gravy paneer."},
                {"name": "Shahi Paneer", "description": "Rich cashew gravy paneer."},
                {"name": "Dal Makhani", "description": "Slow-cooked black lentils."},
                {"name": "Mix Veg Curry", "description": "Seasonal vegetables curry."},
                {"name": "Jeera Rice", "description": "Fragrant cumin rice."},
                {"name": "Veg Biryani", "description": "Spiced layered rice."},
                {"name": "Tandoori Roti", "description": "Clay oven flatbread."},
                {"name": "Butter Naan", "description": "Soft naan with butter."},
                {"name": "Stuffed Kulcha", "description": "Potato-stuffed kulcha bread."},
                {"name": "Chole Bhature", "description": "Spiced chickpeas with bhature."},
                {"name": "Aloo Paratha", "description": "Stuffed pan-fried flatbread."},
                {"name": "Masala Dosa", "description": "Crisp dosa with potato filling."},
                {"name": "Idli Sambar", "description": "Steamed idli with sambar."},
                {"name": "Veg Hakka Noodles", "description": "Indo-Chinese noodles."},
                {"name": "Paneer Tikka", "description": "Grilled marinated paneer cubes."},
                {"name": "Malai Kofta", "description": "Kofta in creamy gravy."},
                {"name": "Veg Fried Rice", "description": "Wok-tossed rice dish."},
            ],
        },
        {
            "title": "Fast Food",
            "items": [
                {"name": "Veg Burger", "description": "Loaded crunchy burger."},
                {"name": "Cheese Burger", "description": "Burger with melted cheese."},
                {"name": "French Fries", "description": "Crispy salted fries."},
                {"name": "Peri Peri Fries", "description": "Fries with peri seasoning."},
                {"name": "Veg Pizza", "description": "Classic veggie pizza."},
                {"name": "Margherita Pizza", "description": "Cheese and basil pizza."},
                {"name": "Paneer Pizza", "description": "Paneer topped pizza."},
                {"name": "Cold Coffee", "description": "Chilled creamy coffee."},
                {"name": "Chocolate Shake", "description": "Rich cocoa milkshake."},
                {"name": "Vanilla Shake", "description": "Smooth vanilla shake."},
                {"name": "Veg Sandwich", "description": "Fresh grilled sandwich."},
                {"name": "Cheese Sandwich", "description": "Toasted cheese sandwich."},
                {"name": "Veg Wrap", "description": "Soft wrap with fillings."},
                {"name": "Paneer Wrap", "description": "Spicy paneer roll."},
                {"name": "Spring Roll", "description": "Crispy veggie rolls."},
                {"name": "Momos", "description": "Steamed dumplings with dip."},
                {"name": "Pasta in Red Sauce", "description": "Tangy tomato pasta."},
                {"name": "Pasta in White Sauce", "description": "Creamy white sauce pasta."},
            ],
        },
    ]

    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for reaching out. Our team will contact you shortly.",
            )
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
