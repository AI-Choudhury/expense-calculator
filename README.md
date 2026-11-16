# Personal Expense Calculator

## Overview

The **Personal Expense Calculator** is a beginner-friendly Python program that calculates the total and average of three personal expenses.

The program asks the user for their name and three expense amounts, performs the necessary calculations, and displays a formatted expense summary.

This project was created as a Python practice exercise to develop fundamental programming skills.

## Features

- Collects the user's name.
- Accepts three expense amounts.
- Calculates the total expenses.
- Calculates the average expense.
- Displays individual expenses in a formatted summary.
- Formats monetary values to two decimal places.

## Technologies Used

- **Python 3**
- Built-in Python functions:
  - `input()`
  - `float()`
  - `print()`

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in Visual Studio Code or your preferred code editor.
4. Open the terminal.
5. Run the following command:

```bash
python expenses.py
```

6. Follow the prompts and enter your name and three expense amounts.

## Example Usage

**Input:**

```text
What is your name? Abida
Enter your first expense: $25.50
Enter your second expense: $40.00
Enter your third expense: $15.50
```

**Output:**

```text
----- Expense Summary -----
Name: Abida
First expense:  $25.50
Second expense: $40.00
Third expense:  $15.50
---------------------------
Total expenses:   $81.00
Average expense:  $27.00
---------------------------
Thank you, Abida!
```

## Python Concepts Practiced

| Concept | Description |
|---|---|
| Variables | Store the user's name and expense amounts. |
| `input()` | Collect information from the user. |
| `float()` | Convert input into decimal numbers. |
| Addition (`+`) | Calculate the total expenses. |
| Division (`/`) | Calculate the average expense. |
| F-strings | Insert variables into formatted messages. |
| Number formatting (`:.2f`) | Display monetary values with two decimal places. |
| `print()` | Display the expense summary. |

## Project Structure

```text
Personal-Expense-Calculator/
│
├── expenses.py
└── README.md
```

## Future Improvements

Potential improvements for this project include:

- Allow users to enter more than three expenses.
- Add expense categories such as groceries, transportation, and entertainment.
- Allow users to enter a monthly budget.
- Calculate the remaining budget after expenses.
- Identify the largest and smallest expenses.

## Author

Created as part of my journey learning Python and developing practical software engineering skills.

---

**Project:** Personal Expense Calculator  
**Language:** Python  
**Level:** Beginner
