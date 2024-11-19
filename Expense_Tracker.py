import json

# Load expenses from file
try:
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = {}

def add_expense():
    category = input("Enter the category (e.g., food, travel): ").strip().lower()
    amount = float(input("Enter the amount: "))
    expenses[category] = expenses.get(category, 0) + amount
    print(f"Added ${amount} to {category}.")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nExpense Summary:")
        for category, total in expenses.items():
            print(f"{category.capitalize()}: ${total:.2f}")
        print()

def save_expenses():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)
    print("Expenses saved successfully!")

# Main menu
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        save_expenses()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
