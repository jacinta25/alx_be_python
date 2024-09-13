#define variables
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
#calculations
monthly_savings = monthly_income -  monthly_expenses
annual_interest = 0.05
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
#print results
print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is: {Projected_Savings}.")
