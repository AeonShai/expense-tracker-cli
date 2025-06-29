# 💸 Expense Tracker CLI

A simple and intuitive command-line tool for tracking your personal expenses.

## 🚀 Features

- Add, list, delete expenses
- View monthly and total summaries
- Categorize expenses
- Set monthly budgets and get warnings if exceeded
- Export data to CSV

## 🧰 Requirements

- Python 3.x

## 🛠️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/expense-tracker-cli.git
cd expense-tracker-cli

📦 Usage
Add an expense

python expense_tracker.py add --description "Coffee" --amount 20 --category "Food"

List all expenses

python expense_tracker.py list

Delete an expense

python expense_tracker.py delete --id 1

View summary

python expense_tracker.py summary
python expense_tracker.py summary --month 6

Set a monthly budget

python expense_tracker.py set-budget --month 6 --amount 500

Export to CSV

python expense_tracker.py export

📁 Data Files

    expenses.json – stores expenses

    budget.json – stores monthly budgets

    expenses.csv – CSV export file
