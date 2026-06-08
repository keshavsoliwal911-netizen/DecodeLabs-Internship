# Expense Tracker

## Description

Expense Tracker is a simple Python console application that allows users to enter multiple expenses and calculates the total amount spent. The program demonstrates fundamental Python concepts such as loops, user input handling, exception handling, type conversion, and accumulators.

## Features

* Add multiple expenses continuously
* Automatically calculate the running total
* Handle invalid inputs using exception handling
* Stop input using a sentinel value (`quit`)
* Display the final total amount spent

## Technologies Used

* Python 3

## How It Works

1. The program asks the user to enter an expense amount.
2. Each valid expense is added to the total.
3. The user can continue entering expenses as needed.
4. Enter `quit` to stop the program.
5. The final total amount spent is displayed.

## Output

```text
=== Expense Tracker ===
Enter your expenses one by one.
Type 'quit' to finish.

Enter expense: 150
Added: ₹150.00
Current Total: ₹150.00

Enter expense: ten
Invalid input! Please enter a valid number.

Enter expense: 10
Added: ₹10.00
Current Total: ₹160.00

Enter expense: quit

===== Expense Summary =====
Total Spent: ₹160.00
Thank you for using Expense Tracker!
```

## Concepts Demonstrated

* Variables
* User Input
* Data Types
* Type Conversion
* Arithmetic Operations
* While Loops
* Exception Handling
* Accumulator Pattern
* Control Flow

## Project Structure

```text
Project_2/
│
├── main.py
└── README.md
```

## Future Improvements

* Expense categories
* Expense history
* Average expense calculation
* Highest and lowest expense tracking
* File-based data storage

## Author

Keshav Soliwal
