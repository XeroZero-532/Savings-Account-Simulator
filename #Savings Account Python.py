#Savings Account Python
monthly_income = float(input("Enter your total monthly income: "))
expenses = []
while True:
    expense = input("Enter an expense (or type 'done' to finish): ")
    if expense.lower() == 'done':
        break
    expense.append(float(expense))
    total_expenses = sum(expenses)
    remaining_balance = monthly_income - total_expenses

    if remaining_balance > 0:
        print(f"You have a surplus of ${remaining_balance:.2f}")
    elif remaining_balance < 0:
        print(f"You have a deficit of ${abs(remaining_balance):.2f}")
    else:
        print ("You have exactly broken even.")