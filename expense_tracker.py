import argparse
import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

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
def add_expense(description, amount):
    expenses = load_expenses()
    new_id = 1 if not expenses else max(e["id"] for e in expenses) + 1
    today = datetime.now().strftime("%d-%m-%Y")
    expense = {
        "id": new_id,
        "date": today,
        "description": description,
        "amount": amount
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

    print(f"{'ID':<4} {'Date':<12} {'Description':<25} {'Amount':>10}")
    print("-" * 55)

    for e in expenses:
        print(f"{e['id']:<4} {e['date']:<12} {e['description']:<25} ${e['amount']:>8.2f}")

#delete func
def delete_expense(expense_id):
    expenses = load_expenses()
    new_expenses = [e for e in expenses if e["id"] != expense_id]

    if len(new_expenses) == len(expenses):
        print(f"Error: ID {expense_id} not found.")
        return
    
    save_expenses(new_expenses)
    print("Expense successfully deleted.")

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

    #args definition
    args = parser.parse_args()
    print(args)

    if args.command == "add":
        if args.amount < 0:
            print("Amount can't be zero")
            return
        add_expense(args.description, args.amount)

    elif args.command == "list":
        list_expense()
    
    elif args.command == "delete":
        delete_expense(args.id)


if __name__ == "__main__":
    main()