# Expense Tracker - Project 2

total = 0

print("=== Expense Tracker ===")
print("Enter your expenses one by one.")
print("Type 'quit' to finish.\n")

while True:
    user_input = input("Enter expense: ")

    if user_input.lower() == "quit":
        break

    try:
        expense = float(user_input)
        total += expense
        print(f"Added: ₹{expense:.2f}")
        print(f"Current Total: ₹{total:.2f}\n")

    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

print("\n===== Expense Summary =====")
print(f"Total Spent: ₹{total:.2f}")
print("Thank you for using Expense Tracker!")