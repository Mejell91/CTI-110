#Jemell Rodgers
#P3HW2
#March 21 2024
#Calculating Gross Pay

employee_name = input("Enter employee's name: ")

hours_wrk = float(input("Enter number of hours worked: "))

pay_rate = float(input("Enter employee's pay rate: "))


overtime_hours = max(0, hours_wrk - 40)

regular_hours = hours_wrk - overtime_hours

overtime_pay = 0
if overtime_hours > 0:
    overtime_pay = overtime_hours * pay_rate * 1.5

regular_pay = regular_hours * pay_rate

gross_pay = regular_pay + overtime_pay

print("Employee name:", employee_name)
print("Hours Worked   Pay Rate")
print("-------------  --------")
print("OverTime       ", "{:.2f}".format(overtime_hours))
print("OverTime Pay   ", "${:.2f}".format(overtime_pay))
print("RegHour Pay    ", "${:.2f}".format(regular_pay))

print("Gross Pay")
print("${:.2f}".format(gross_pay))
