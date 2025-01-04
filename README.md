# Personal Expense Tracker

## Description
A console-based Python application to manage and track personal expenses. Users can add expenses, view summaries, and get monthly breakdowns. All data is stored persistently in `expenses.txt`.

## Features
- Add Expense: Record expense details (category, amount, and date).
- View Expenses: View expenses grouped by categories.
- Monthly Summary: Get a summary of expenses by month and category.
- Persistent storage with file handling.

## How to Run
1.Clone this repository:
   
    git clone https://github.com/green119/Personal-Expense-Tracker

2.Navigate to the project directory:

    cd Personal-Expense-Tracker

3.Run the application:
   
     python expense_tracker.py


## Example Usage
### Main Menu
```text
Welcome to Personal Expense Tracker!
1. Add Expense
2. View Expenses
3. Monthly Summary
4. Exit
Enter your choice: 1
```
### Adding an Expense
```text
Enter category (e.g., Food, Travel): Food
Enter amount: 200
Enter date (YYYY-MM-DD): 2024-12-23
Expense added successfully!
```
### Viewing Expenses
```text
Expenses:
Food:
  1. Amount: 200.00 - Date: 2024-12-23

Travel:
  No expenses recorded.
```
### Monthly Summary
```text
Monthly Summary (December 2024):
Total Expenses: 200.00
By Category:
  Food: 200.00
  Travel: 0.00
```


## Project Structure
```plaintext
PersonalExpenseTracker/
├── expense_tracker.py  # Main Python script
├── expenses.txt        # Persistent storage file (created automatically)
├── README.md           # Project documentation
```


## Dependencies
- Python 3.x

## Author
Harshit Goyal
