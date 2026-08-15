import os
from datetime import datetime
from auth import sign_up
from auth import login


FOOD = {
    1: {"name": "rice", "price": 250, "unit": "spoon"},
    2: {"name": "jollof rice", "price": 250, "unit": "spoon"},
    3: {"name": "fried rice", "price": 250, "unit": "spoon"},
    4: {"name": "beans", "price": 250, "unit": "spoon"},
    5: {"name": "yam", "price": 250, "unit": "spoon"},
    6: {"name": "fish", "price": 250, "unit": "piece"},
    7: {"name": "meat", "price": 250, "unit": "piece"},
    8: {"name": "egg", "price": 250, "unit": "piece"},
    9: {"name": "bottle water", "price": 100, "unit": "piece"},
    10: {"name": "soft drink", "price": 200, "unit": "piece"},
    11: {"name": "juice", "price": 250, "unit": "piece"},
}


def show_welcome():
    os.system("clear")
    print("========= Welcome to GetFOOD CLI ========")
    input("pls press enter to continue....")


def display_food(FOOD):
    print("\n===== GETFOOD MENU =====")
    for number, details in FOOD.items():
        label = "per spoon" if details["unit"] == "spoon" else "per piece"
        print(f"{number}. {details['name']} - {details['price']} {label}")

def pick_item(FOOD):
    display_food(FOOD)

    choice = input("Enter the number of the food you want: ").strip()
    if not choice.isdigit():
        print("That is not a valid number, try again")
        return None

    choice = int(choice)

    if choice not in FOOD:
        print("That number is not on the menu, try again")
        return None

    return choice


def get_quantity_total(item_name, item_price, unit):
    word = "spoons" if unit == "spoon" else "pieces"

    while True:
        qty_input = input(f"How many {word} of {item_name} do you want: ").strip()

        if not qty_input.isdigit():
            print("That is not a valid number, try again")
            continue

        qty = int(qty_input)

        if qty <= 0:
            print("Quantity must be at least 1, try again")
            continue

        total = qty * item_price
        print(f"{qty} {word} of {item_name} = {total}")
        return qty, total


def order_food(FOOD):
    cart = []

    while True:
        choice = pick_item(FOOD)

        if choice is None:
            continue

        item_name = FOOD[choice]["name"]
        item_price = FOOD[choice]["price"]
        unit = FOOD[choice]["unit"]

        qty, total = get_quantity_total(item_name, item_price, unit)

        cart.append({"name": item_name, "qty": qty, "unit": unit, "total": total})

        more = input("Type done to finish, or press enter to add more: ").strip().lower()
        if more == "done":
            break

    return cart


def calculate_total(cart):
    grand_total = 0
    for entry in cart:
        grand_total += entry["total"]
    return grand_total


def choose_payment_method():
    print("\n===== PAYMENT METHOD =====")
    print("1. Cash")
    print("2. Card")
    print("3. Transfer")

    while True:
        choice = input("Choose your payment method: ").strip()
        if choice == "1":
            return "Cash"
        elif choice == "2":
            return "Card"
        elif choice == "3":
            return "Transfer"
        else:
            print("Invalid choice, try again")


def print_receipt(username, cart, grand_total, payment_method):
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n===== RECEIPT =====")
    print(f"Name: {username}")
    print(f"Time: {order_time}")
    print("--------------------")

    for entry in cart:
        word = "spoons" if entry["unit"] == "spoon" else "pieces"
        print(f"{entry['name']} x{entry['qty']} {word} = {entry['total']}")

    print("--------------------")
    print(f"Total: {grand_total}")
    print(f"Payment method: {payment_method}")
    print("--------------------")
    print("Your order is on the way, it will arrive in 20 minutes.")


def main():
    show_welcome()
    username = None

    while True:
        print("======= WELCOME ========")
        print("\n1. Sign up ")
        print("2. Login")
        print("===============================")

        user = input("Enter a choice : ")
        if user == "1":
            result = sign_up()
            if result:
                username = result
                break
        elif user == "2":
            result = login()
            if result:
                username = result
                break
        else:
            print("Invalid input ")

    cart = order_food(FOOD)
    grand_total = calculate_total(cart)
    payment_method = choose_payment_method()
    print_receipt(username, cart, grand_total, payment_method)


if __name__ == "__main__":
    main()