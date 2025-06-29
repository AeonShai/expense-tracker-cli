import argparse
import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"
BUDGET_FILE = "budget.json"

def load_budgets():
    if not os.path.exists(BUDGET_FILE):
        return {}
    with open (BUDGET_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_budgets(budgets):
    with open(BUDGET_FILE, "w") as f:
        json.dump(budgets, f, indent=4)
#Load file
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open (DATA_FILE, "r") as f:
        return json.load(f)

#Save expenses
def save_expenses(expenses):
    with open (DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

#Add func
def add_expense(description, amount, category=None):
    expenses = load_expenses()
    new_id = 1 if not expenses else max(e["id"] for e in expenses) + 1
    today = datetime.now().strftime("%d-%m-%Y")
    expense = {
        "id": new_id,
        "date": today,
        "description": description,
        "amount": amount,
        "category": category or "Expense"
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Exppense successfully added (ID: {new_id})")

#list func
def list_expense():
    expenses = load_expenses()
    if not expenses:
        print("Expenses not found")
        return

    print(f"{'ID':<4} {'Date':<12} {'Description':<25} {'Category':<15} {'Amount':>10}")
    print("-" * 70)

    for e in expenses:
        print(f"{e['id']:<4} {e['date']:<12} {e['description']:<25} {e.get('category', 'Expense'):<15} ${e['amount']:>8.2f}")

#delete func
def delete_expense(expense_id):
    expenses = load_expenses()
    new_expenses = [e for e in expenses if e["id"] != expense_id]

    if len(new_expenses) == len(expenses):
        print(f"Error: ID {expense_id} not found.")
        return
    
    save_expenses(new_expenses)
    print("Expense successfully deleted.")

#summary func
def summary_expense(month=None):
    expenses = load_expenses()
    total = 0

    for e in expenses:
        try:
            expense_date = datetime.strptime(e["date"], "%d-%m-%Y")
        except ValueError:
            print(f"Invalid date format: {e['date']}")
            continue

        if month:
            if expense_date.month == month and expense_date.year == datetime.now().year:
                total += e["amount"]
        else:
            total += e["amount"]

    if month:
        print(f"Summary for {month}: ${total:.2f}")
        budgets = load_budgets()
        budget_amount = budgets.get(str(month))
        if budget_amount and total > budget_amount:
            print(f"Warn: Your budget for {month} is limited.")
    else:
        print(f"Sum: ${total:.2f}")

def main():
    parser = argparse.ArgumentParser(prog="expense-tracker", description="Simple expense tracker")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    #add command
    add_parser = subparsers.add_parser("add", help="Add new log")
    add_parser.add_argument("--description", required=True, help="Description")
    add_parser.add_argument("--amount", required=True, type=float, help="Amount")

    #list command
    subparsers.add_parser("list", help="Listing")

    #delete command
    delete_parser = subparsers.add_parser("delete", help="Delete")
    delete_parser.add_argument("--id", required=True, type=int, help="ID of deleting op")

    #summary command
    summary_parser = subparsers.add_parser("summary", help="Summary")
    summary_parser.add_argument("--month", type=int, help="Month filter")

    #category command
    add_parser.add_argument("--category", required=False, help="Category (exp: Food,Travel, etc...)")

    #budget command
    budget_parser = subparsers.add_parser("set-budget", help="Set monthly budget")
    budget_parser.add_argument("--month", required=True, type=int, help="Month number (1-12)")
    budget_parser.add_argument("--amount", required=True, type=float, help="Budget amount for expense")
    #args definition
    args = parser.parse_args()
    print(args)

    if args.command == "add":
        if args.amount < 0:
            print("Amount can't be zero")
            return
        add_expense(args.description, args.amount, args.category)

    elif args.command == "list":
        list_expense()
    
    elif args.command == "delete":
        delete_expense(args.id)
    
    elif args.command == "summary":
        if args.month:
            if not (1 <= args.month <= 12):
                print("Error: Month should be in 1-12")
                return
            summary_expense(month=args.month)
        else:
            summary_expense()
    elif args.command == "set-budget":
        if not (1 <= args.month <= 12):
            print("Error: Month must be between 1 and 12")
            return
        budgets = load_budgets()
        budgets[str(args.month)] = args.amount
        save_budgets(budgets)
        print(f"Bütçe ayarlandı: Ay {args.month} için ${args.amount:.2f}")
        


if __name__ == "__main__":
    main()