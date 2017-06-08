grades =int(input("Enter students grade"))
total = 0
counter = 0
while grades > 0:

    total+=grades
    counter+=1
    avg=total/counter
    grades = int(input("Enter students grade"))

print("The average grade is",avg)