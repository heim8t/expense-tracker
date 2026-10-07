# Project: Expense Tracker | Installment 3: The Tracker Does Math
# Author: Vinsel John M. Ramones
# Description: Prints the landing page, asks for a name and two expenses, then computes subtotal, average, tax, grand total and budget.

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

# Running subtotal starts at 0 and grows right after each amount is read
subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# Average comes from the subtotal
average = subtotal / 2

# Tax rate is typed as a whole number (12 means 12%)
tax_percent = float(input("Tax rate %? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

# Budget check
budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

# Summary: tabs line up the values
print()
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

# Footer
print("Made by: Vinsel John M. Ramones | Installment 3")