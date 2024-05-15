#Jemell Rodgers
#P4LAB2
#March 27 2024
#Use a while loop

#Get two integer value from user
var1 = int(input("Enter the smaller integer: "))
var2 = int(input("Enter the larger integer: "))

#While var1 is larger, allow the user to re-enter the values
while var1 >= var2:
    print("Wrong try again")
    var1 = int(input("Enter the smaller integer: "))
    var2 = int(input("Enter the larger integer: "))

#While loop has broken. Values are correct.
for num in range(var1, var2+1, 5):
    print(num, end = " ")
