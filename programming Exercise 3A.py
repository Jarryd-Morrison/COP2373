from functools import reduce

def get_user_expenses():
    expenses = []
    
    while True:
        expense_type = input("Enter the type of expense (or type 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
        except ValueError:
            print("Please enter a valid number for the amount.")
            continue
        
        expenses.append((expense_type, amount))
    
    return expenses

def analyze_expenses(expenses):
    if not expenses:
        print("No expenses were provided.")
        return

    # Calculate total expenses using reduce
    total_expense = reduce(lambda acc, x: acc + x[1], expenses, 0)
    
    # Find the highest expense using reduce
    highest_expense = reduce(lambda acc, x: x if x[1] > acc[1] else acc, expenses)
    
    # Find the lowest expense using reduce
    lowest_expense = reduce(lambda acc, x: x if x[1] < acc[1] else acc, expenses)

    print("\n--- Expense Summary ---")
    print(f"Total expenses: ${total_expense:.2f}")
    print(f"Highest expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

def main():
    expenses = get_user_expenses()
    analyze_expenses(expenses)


main()
