# GetFood CLI

A command line food ordering application built in Python. Users can sign up or log in with a hashed and salted password, browse a food menu, add items to a cart, choose a payment method, and receive a printed receipt.

## Features

- User authentication with SHA-256 password hashing and salting
- Passwords and usernames stored in a plain text file, no database or JSON used
- Food menu with items priced either per spoon or per piece
- Ordering loop that lets users keep adding items until they choose to stop
- Payment method selection, cash, card, or transfer
- Receipt showing the registered username, order time, items ordered, total cost, payment method, and delivery message

## Files

- `auth.py`, handles user signup and login, including password hashing and salting
- `getfood.py`, main program, handles the menu, ordering, payment, and receipt

## How to run

Make sure `auth.py` and `getfood.py` are in the same folder, then run:

```
python getfood.py
```

## How it works

On first run, users can sign up with a username at least 5 characters long and a password. The password is salted and hashed with SHA-256 before being saved, plain text passwords are never stored. Returning users can log in with the same credentials.

After logging in, the food menu is displayed with a number next to each item. Users pick an item by number, choose a quantity, either spoons or pieces depending on the item, and repeat until they type done. The program then totals the cart, asks for a payment method, and prints a receipt with the time the order was placed.

## Built with

- Python
- hashlib for password hashing
- os for salting and file handling
- datetime for order timestamps

## Author

Built by Hazeem  Bankole as a self directed Python project.
