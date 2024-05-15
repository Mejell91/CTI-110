#Jemell Rodgers
#2/22/2024
#P1HW2
#Calculating travel budget expenses


budget = int(input("Enter your budget: "))

gas = int(input("Enter the amount you will spend on gas: "))

destination = int(input("Enter your travel destination"))

accomodation_expense = int(input("Enter the amount you will spend on accomdation: "))

food_expenses = int(input("Enter the amount you will spend on food: "))

total_expenses = gas_expense + accomodation_expense + food_expense

remaining_budget = budget - total_expenses

print("This program calculates and displays travel expenses")
print("Enter your budget: ", budget)
print("Enter the amount you will spend on gas: ", gas)
print("Enter your travel destination: ", destination)
print("Enter the amount you will spend on accomdation: ", accomodation_expense)
print("Enter the amount you will spend on food: ", food_expenses,)
print("total cost", total_expenses)
print("remaining budget: ", remaining_budget)
