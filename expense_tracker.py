import csv
from datetime import datetime

FILE_NAME = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


# Create CSV file if it does not exist
def create_file():
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8"):
            pass
    except FileNotFoundError:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


# Load all expenses from CSV
def load_expenses():
    create_file()

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


# Add a new expense
def add_expense():
    print("\n--- Add Expense ---")

    # Date validation
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")

    # Category
    category = input("Enter category (Food/Travel/Study/Bills/Fun): ").strip()

    while category == "":
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    # Description
    description = input("Enter description: ").strip()

    while description == "":
        print("Description cannot be empty.")
        description = input("Enter description: ").strip()

    # Amount validation
    while True:
        amount = input("Enter amount: ")

        try:
            amount = float(amount)

            if amount < 0:
                print("Amount cannot be negative.")
            elif amount == 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Save expense
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        writer.writerow({
            "date": date,
            "category": category,
            "description": description,
            "amount": f"{amount:.2f}"
        })

    print("Expense added successfully!")


# Display expenses in table format
def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "-" * 75)
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>15}")
    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<25}"
            f"₹{float(expense['amount']):>13.2f}"
        )

    print("-" * 75)


# View all expenses
def view_all():
    print("\n--- All Expenses ---")

    expenses = load_expenses()
    display_expenses(expenses)


# Filter expenses
def filter_expenses():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses available.")
        return

    print("\n--- Filter Expenses ---")
    print("1. Filter by Category")
    print("2. Filter by Month")
    print("3. Back")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ").strip().lower()

        filtered = []

        for expense in expenses:
            if expense["category"].lower() == category:
                filtered.append(expense)

        print(f"\nExpenses for category: {category}")
        display_expenses(filtered)

    elif choice == "2":
        while True:
            month = input("Enter month (YYYY-MM): ")

            try:
                datetime.strptime(month, "%Y-%m")
                break
            except ValueError:
                print("Invalid month. Please use YYYY-MM format.")

        filtered = []

        for expense in expenses:
            if expense["date"][:7] == month:
                filtered.append(expense)

        print(f"\nExpenses for month: {month}")
        display_expenses(filtered)

    elif choice == "3":
        return

    else:
        print("Invalid choice.")


# Show summary
def show_summary():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses available for summary.")
        return

    print("\n--- Expense Summary ---")

    category_totals = {}

    grand_total = 0
    biggest_expense = None

    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])

        # Category total
        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

        # Grand total
        grand_total += amount

        # Biggest expense
        if biggest_expense is None:
            biggest_expense = expense
        elif amount > float(biggest_expense["amount"]):
            biggest_expense = expense

    print("\nTotal spending by category:")

    for category, total in category_totals.items():
        print(f"{category:<15} ₹{total:.2f}")

    print("\nGrand Total:")
    print(f"₹{grand_total:.2f}")

    print("\nBiggest Single Expense:")

    print(
        f"Date: {biggest_expense['date']}\n"
        f"Category: {biggest_expense['category']}\n"
        f"Description: {biggest_expense['description']}\n"
        f"Amount: ₹{float(biggest_expense['amount']):.2f}"
    )


# Main menu
def main():
    create_file()

    while True:
        print("\n===================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("===================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Expense Summary")
        print("5. Quit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_all()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            show_summary()

        elif choice == "5":
            print("\nThank you for using Personal Expense Tracker!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1 to 5.")


# Start the program
if __name__ == "__main__":
    main()