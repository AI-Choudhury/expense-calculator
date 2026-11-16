
# Ask the user for their name.
# input() collects the user's response as a string.
name = input("What is your name? ")

# Ask the user to enter their first expense.
# float() converts the input from a string into a decimal number.
expense1 = float(input("Enter your first expense: $"))

# Ask the user to enter their second expense.
expense2 = float(input("Enter your second expense: $"))

# Ask the user to enter their third expense.
expense3 = float(input("Enter your third expense: $"))

# Calculate the total of all three expenses.
# The + operator adds the three expense amounts together.
total = expense1 + expense2 + expense3

# Calculate the average expense.
# Divide the total by 3 because there are three expenses.
average = total / 3

# Display a heading for the expense summary.
print("\n----- Expense Summary -----")

# Display the user's name.
print(f"Name: {name}")

# Display each individual expense.
# :.2f formats each amount to exactly two decimal places.
print(f"First expense:  ${expense1:.2f}")
print(f"Second expense: ${expense2:.2f}")
print(f"Third expense:  ${expense3:.2f}")

# Display the total and average expenses.
print("---------------------------")
print(f"Total expenses:   ${total:.2f}")
print(f"Average expense:  ${average:.2f}")

# Display a closing message.
print("---------------------------")
print(f"Thank you, {name}!")
