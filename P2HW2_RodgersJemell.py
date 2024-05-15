#Jemell Rodgers
#P2HW2
#Mar 3 2024
#Listing grades as a list

grade1 = float(input("Enter grade for Module 1: "))

grade2 = float(input("Enter grade for Module 2: "))

grade3 = float(input("Enter grade for Module 3: "))

grade4 = float(input("Enter grade for Module 4: "))

grade5 = float(input("Enter grade for Module 5: "))

grade6 = float(input("Enter grade for Module 6: "))

lowest_grades = min(grade1 ,grade2,grade3,grade4, grade5, grade6)
highest_grades = max(grade1 ,grade2,grade3,grade4, grade5, grade6)
sum_grades = grade1 + grade2 + grade3 + grade4 + grade5+ grade6
avg_grades = sum_grades / 6

print(f"Lowest Grade: {lowest_grades}")
print(f"Highest Grade: {highest_grades}")
print(f"Sum of Grades: {sum_grades}")
print(f"Average: {avg_grades:.2f}")
