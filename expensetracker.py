import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    title = input("Enter expense title: ")
    amount = float(input("Enter amount (PKR): "))
    expenses.append({"title": title, "amount": amount})
    save_expenses(expenses)
    print("✅ Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = 0
    print("\n=== Expense List ===")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['title']} — Rs.{e['amount']}")
        total += e['amount']
    print(f"\nTotal Spent: Rs.{total}")

def delete_expense(expenses):
    view_expenses(expenses)
    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses(expenses)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("Saving and exiting... 👋")
            save_expenses(expenses)
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
