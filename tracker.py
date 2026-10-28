# Expense Tracker - Installment 5: The Menu Comes Alive
# Author: Junsay, Geme Earl C.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

subtotal = 0.0
count = 0

print(f"\nWelcome, {name}!")

menu = """
MAIN MENU
    [1] Add an expense
    [2] View all expenses (coming soon)
    [3] Show total spent
    [4] Exit
"""

while True:
    print(menu)
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("Huge expense - are you sure?")
        elif amount > 100:
            print("Big expense.")
        elif amount > 50:
            print("Moderate expense.")
        else:
            print("Small expense.")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax

        print("\nSUMMARY")
        print(f"{'Expenses:':<20}{count}")
        print(f"{'Subtotal:':<20}${subtotal:.1f}")
        print(f"{'Tax (' + str(tax_percent) + '%):':<20}${tax:.1f}")
        print(f"{'Grand total:':<20}${total:.1f}")

        if total > budget:
            print(f"Over budget by ${total - budget:.1f}!")
        elif total > budget * 0.9:
            print(f"Careful: only ${budget - total:.1f} left.")
        else:
            print(f"Within budget. ${budget - total:.1f} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print(f"Made by: {name} | Installment 5")
        print("-" * 40)
        break

    else:
        print("Please choose 1, 2, 3 or 4.")