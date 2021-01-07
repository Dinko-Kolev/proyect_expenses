def calculate_budget_left(profile, expenses):
    expenses = expenses
    budjet = profile.budget
    left = float(budjet)
    for expense in expenses:
        left -= float(expense.price)
    return left
