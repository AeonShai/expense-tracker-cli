# 💸 Expense Tracker CLI

A simple and intuitive command-line tool for tracking your personal expenses.

## 🚀 Features

- Add, list, and delete expenses
- View summaries (overall and monthly)
- Categorize expenses
- Set monthly budgets with warning
- Export data to CSV

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/expense-tracker-cli.git
cd expense-tracker-cli
```

Run with Python:

```bash
python expense_tracker.py --help
```

## 🧾 Usage

### ➕ Add an expense
```bash
python expense_tracker.py add --description "Lunch" --amount 30 --category "Food"
```

### 📋 List expenses
```bash
python expense_tracker.py list
```

### ❌ Delete an expense
```bash
python expense_tracker.py delete --id 1
```

### 📊 View summary
```bash
python expense_tracker.py summary
python expense_tracker.py summary --month 6
```

### 💰 Set monthly budget
```bash
python expense_tracker.py set-budget --month 6 --amount 500
```

### 📤 Export to CSV
```bash
python expense_tracker.py export
```

## 📁 Data Files

- `expenses.json` – stores your expense records
- `budget.json` – stores monthly budgets
- `expenses.csv` – CSV export output
