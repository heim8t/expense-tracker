# Project: Expense Tracker | Installment 2: Talking to the User
# Author: Vinsel John M. Ramones
# Description: Prints the landing page, then asks the user for a name and two expenses and prints a summary.

# Top banner
print("=" * 40)

# Title and tagline (indented with tabs)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")

# Bottom banner
print("=" * 40)

# Main menu: tabs line up every "(coming soon)" in one column
print("\nMAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")

# Greeting
name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

# Ask for two expenses (amounts stored as numbers)
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

# Calculations
total = amount1 + amount2
average = total / 2

# Summary: tabs line up the values
print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)

# Footer
print("Made by: Vinsel John M. Ramones | Installment 2")