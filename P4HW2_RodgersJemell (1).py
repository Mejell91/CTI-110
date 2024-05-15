#Jemell Rodgers
#4/8/2024
#P4HW2

num_employees = int(input("Enter the number of employees: "))

total_overtime_pay = 0
total_regular_pay = 0
total_pay_all_employees = 0

for _ in range(num_employees):
    employee_name = input("Enter employee's name: ")
    hours_wrk = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    overtime_hours = max(0, hours_wrk - 40)
    regular_hours = hours_wrk - overtime_hours
    overtime_pay = 0


overtime_pay = overtime_hours * pay_rate * 1.5
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

total_overtime_pay = total_overtime_pay + overtime_pay
total_regular_pay = total_regular_pay + regular_pay
total_pay_all_employees = total_pay_all_employees + gross_pay

print("Employee name:", employee_name)
print("Hours Worked Pay Rate")
print("------------- --------")
print("OverTime ", "{:.2f}".format(overtime_hours))
print("OverTime Pay ", "${:.2f}".format(overtime_pay))
print("RegHour Pay ", "${:.2f}".format(regular_pay))
print("Gross Pay")
print("${:.2f}".format(gross_pay))

print("\n=== Total Payments ===")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Pay for All Employees: ${total_pay_all_employees:.2f}")


#P4HW2 code starts here

