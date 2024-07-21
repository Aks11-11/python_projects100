import datetime
import json
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': str(datetime.date.today())
        }
        self.expenses.append(expense)
        print(f"Added expense: {expense}")

    def view_expenses(self):
        for expense in self.expenses:
            print(expense)

    def view_expenses_by_category(self, category):
        category_expenses = [exp for exp in self.expenses if exp['category'] == category]
        for expense in category_expenses:
            print(expense)

    def total_expense(self):
        total = sum(exp['amount'] for exp in self.expenses)
        print(f"Total expense: ${total:.2f}")
        return total

    def save_expenses(self, filename="expenses.json"):
        with open(filename, 'w') as file:
            json.dump(self.expenses, file)
        print(f"Expenses saved to {filename}")

    def load_expenses(self, filename="expenses.json"):
        try:
            with open(filename, 'r') as file:
                self.expenses = json.load(file)
            print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            print(f"No file named {filename} found. Starting with an empty expense list.")


def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()

    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View expenses by category")
        print("4. View total expense")
        print("5. Save expenses")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description (optional): ")
            tracker.add_expense(amount, category, description)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            category = input("Enter the category: ")
            tracker.view_expenses_by_category(category)
        elif choice == "4":
            tracker.total_expense()
        elif choice == "5":
            filename = input("Enter the filename to save expenses (default: expenses.json): ")
            if not filename:
                filename = "expenses.json"
            tracker.save_expenses(filename)
        elif choice == "6":
            tracker.save_expenses()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
