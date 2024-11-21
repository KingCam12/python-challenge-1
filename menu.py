# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list
order_list = []

# Launch the store and greet the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so create a continuous loop
place_order = True
while place_order:
    # Ask the customer which menu category they want to order from
    print("\nFrom which menu would you like to order?")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get the customer's input
    menu_category = input("\nType menu number: ")

    if menu_category.isdigit() and int(menu_category) in menu_items:
        menu_category_name = menu_items[int(menu_category)]
        print(f"\nYou selected {menu_category_name}. What would you like to order?")
        
        # Print menu items
        i = 1
        menu_items = {}
        print("\nItem # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    num_item_spaces = 24 - len(key + " - " + subkey)
                    print(f"{i}      | {key} - {subkey}{' ' * num_item_spaces} | ${subvalue:.2f}")
                    menu_items[i] = {"Item name": f"{key} - {subkey}", "Price": subvalue}
                    i += 1
            else:
                num_item_spaces = 24 - len(key)
                print(f"{i}      | {key}{' ' * num_item_spaces} | ${value:.2f}")
                menu_items[i] = {"Item name": key, "Price": value}
                i += 1

        # Get menu item number
        menu_item = input("\nType menu item number: ")

        if menu_item.isdigit() and int(menu_item) in menu_items:
            selected_item = menu_items[int(menu_item)]
            item_name = selected_item["Item name"]
            item_price = selected_item["Price"]

            # Ask for quantity
            quantity = input(f"How many {item_name}s would you like? ")
            if not quantity.isdigit():
                quantity = 1
            else:
                quantity = int(quantity)

            # Add to order list
            order_list.append({"Item name": item_name, "Price": item_price, "Quantity": quantity})
            print(f"\n{quantity} x {item_name} added to your order.")
        else:
            print("Invalid menu item number.")
    else:
        print("Invalid menu category.")

    # Ask if the customer wants to order more
    while True:
        keep_ordering = input("\nWould you like to order anything else? (Y)es or (N)o: ").lower()
        if keep_ordering == 'y':
            break
        elif keep_ordering == 'n':
            place_order = False
            break
        else:
            print("Please enter 'Y' or 'N'.")

# Print the final order
print("\nThis is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]
    item_spaces = 24 - len(item_name)
    print(f"{item_name}{' ' * item_spaces} | ${price:.2f} | {quantity}")

# Calculate and print total cost
total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)
print(f"\nTotal cost: ${total_cost:.2f}")
