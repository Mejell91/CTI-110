#Jemell Rodgers
#2/22/2024
#P2HW1
#Calculating travel budget expenses

#Get travel budget input
budget = float (input("Enter your budget: "))

gas = float (input("Enter the amount you will spend on gas: "))

destination = (input("Enter your travel destination? "))

accomodation_expense = float (input("Enter the amount you will spend on accomdation: "))

food_expenses = float (input("Enter the amount you will spend on food: "))

#Calculate travel budget
total_expenses = gas + accomodation_expense + food_expenses

remaining_budget = budget - total_expenses

#Output budget cost and remaining
print("Travel Expenses")
print(f"Budget: ${budget}")
print(f"Gas: ${gas}")
print(f"Destination: {destination}")
print(f"Accommodation: ${accomodation_expense}")
print(f"Food: ${food_expenses}")
print(f"Total Cost: ${total_expenses}")
print(f"Remaining Budget: ${remaining_budget}")
