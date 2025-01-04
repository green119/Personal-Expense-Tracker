import os
from datetime import datetime

EXPENSES_FILE = "expenses.txt"

def main_menu():
    print("\nWelcome to Personal Expense Tracker!")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        monthly_summary()
    elif choice == "4":
        print("Thank you for using the Personal Expense Tracker. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")


def add_expense():
    category = input("Enter category (e.g., Food, Travel): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")
        return

    with open(EXPENSES_FILE, "a") as file:
        file.write(f"{category},{amount},{date}\n")

    print("Expense added successfully!")


def view_expenses():
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    categories = {}
    for category, amount, date in expenses:
        if category not in categories:
            categories[category] = []
        categories[category].append((amount, date))

    print("\nExpenses:")
    for category, records in categories.items():
        print(f"\n{category}:")
        if records:
            for amount, date in records:
                print(f"  Amount: {amount:.2f} - Date: {date}")
        else:
            print("  No expenses recorded.")


def monthly_summary():
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    try:
        month_year = input("Enter month and year (YYYY-MM): ").strip()
        datetime.strptime(month_year, "%Y-%m")
    except ValueError:
        print("Invalid format. Please enter in YYYY-MM format.")
        return

    monthly_expenses = [exp for exp in expenses if exp[2].startswith(month_year)]

    if not monthly_expenses:
        print(f"No expenses recorded for {month_year}.")
        return

    total_expenses = sum(amount for _, amount, _ in monthly_expenses)
    categories = {}
    for category, amount, _ in monthly_expenses:
        if category not in categories:
            categories[category] = 0
        categories[category] += amount

    print(f"\nMonthly Summary ({month_year}):")
    print(f"Total Expenses: {total_expenses:.2f}")
    print("By Category:")
    for category, total in categories.items():
        print(f"  {category}: {total:.2f}")


def read_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []

    expenses = []
    with open(EXPENSES_FILE, "r") as file:
        for line in file:
            try:
                category, amount, date = line.strip().split(",")
                expenses.append((category, float(amount), date))
            except ValueError:
                print("Skipping invalid entry in expenses file.")
    return expenses


if __name__ == "__main__":
    while True:
        main_menu()