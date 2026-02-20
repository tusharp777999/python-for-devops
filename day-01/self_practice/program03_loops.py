#To do the repeatative task we should use loops concept in this scenario as below we are using the for loop.
for i in range(2):#It starts with 0 and the range it shows is 0 to 4.
    environment = input("Enter the Environment: ")
    print("The user input is: ", environment)

    #if-else is a Conditional Statement which works on boolean condition, Here we are using conditonal operators like ==, !=, <=, >= etc.
    if environment == "PROD":
        print("Don't deploy on Friday.")
    elif environment == "UAT":
        print("Take backup and test well.")
    else:
        print("Safe to deploy on any day.")

print(range(5))#It shows the range.

#To print range values:
for i in range(5):
    print(i)

#Print tables for given number:
number = int(input("Enter the number for which you want tables: "))#Take the number which is in string format converted into integer using type-casting.
print(f"Table for {number}:")#Used "f" within print() throug which we can define a dynamic variable value in static string. It is called as string format.
for i in range(1, 11):
    print(f"{number} x {i} = ", number * i)

#while loop:
choice = input("Enter your choice (Press y/n): ")
while choice != "n":#It executes until the condition is not getting false.
    number = int(input("Enter the number for which you want tables: "))
    print(f"Table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = ", number * i)
    choice = input("Enter your choice (Press y/n): ")