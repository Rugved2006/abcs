import time

MENU = {
    "Indian": {
        1: {"name": "Butter Naan", "price": 100},
        2: {"name": "Chicken Tikka Masala", "price": 450},
        3: {"name": "Paneer Makhani", "price": 380},
        4: {"name": "Veg Biryani", "price": 320},},
    "Chinese": {
        1: {"name": "Veg Spring Rolls", "price": 220},
        2: {"name": "Hakka Noodles", "price": 280},
        3: {"name": "Chilli Paneer", "price": 350},
        4: {"name": "Manchurian Dry", "price": 300},},
    "Italian": {
        1: {"name": "Margherita Pizza", "price": 550},
        2: {"name": "Spaghetti Aglio e Olio", "price": 420},
        3: {"name": "Veg Lasagna", "price": 480},
        4: {"name": "Tiramisu (Dessert)", "price": 290},}}

SERVICE_CHARGE_RATE = 0.10
GST_RATE = 0.18
BULK_DISCOUNT_RATE = 0.10
BULK_DISCOUNT_THRESHOLD = 3500

def display_menu():
    print("\n" + "🌟" * 25)
    print("  Welcome to The Beginner's Cafe! Today's Delights:  ")
    print("🌟" * 25)
    for category, items in MENU.items():
        print(f"\n--- 🇮🇳 🇨🇳 🇮🇹 {category} Specials ---")
        for item_num, item_details in items.items():
            name = item_details["name"]
            price = item_details["price"]
            print(f"[{item_num}] {name:<25} ............ Rs. {price:>.2f}")

def take_order():
    order = []
    print("\n--- Time to Take Your Order! ---")

    while True:
        print("\nWhat looks good to you? (Indian, Chinese, Italian)")
        category_choice = input("Enter cuisine to browse (or type 'Done' to finalize): ").strip().title()

        if category_choice == "Done":
            break

        if category_choice not in MENU:
            print("Oops! We don't have that cuisine. Please try one of our specialties.")
            continue

        print(f"\n--- Showing Our Best: {category_choice} Menu ---")
        category_items = MENU[category_choice]
        for num, details in category_items.items():
            print(f"[{num}] {details['name']:<25} ............ Rs. {details['price']:>.2f}")

        while True:
            item_input = input("\nEnter item number to add, 'C' to check another cuisine, or 'F' to finish and print
