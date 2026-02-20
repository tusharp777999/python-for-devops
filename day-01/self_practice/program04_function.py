'''
Function is a block of code. Which helps you to write cleaner code and separates the logic which helps in debugging and reuse of that code.
Function defination means we defined the function using "def" keyword and given a name as "sum_of_number" with round parenthesis which shows it is a function and the round 
parenthesis can have arguments as well to provide some input to the function
'''
def sum_of_number():#To define the function.
    first = int(input("Enter first number: "))#Logic inside the function you can take any logic in it as per your needs.
    second = int(input("Enter second number: "))

    sum = first + second
    print(sum)

sum_of_number()#It is function calling to call the function.

#To call the function based on the condition like we need to call based on the environment Ex. QA, UAT, PROD.
environment = input("Enter the environment: ")
print("The entered environment is: ", environment)

if environment == "PROD":
    sum_of_number()
else:
    print("Provided environment is not PROD it is: ", environment)

#Call backup method based on some particular week day which is working day.
def backup():
    print("Backup script is started!!!")

weekday = input("Enter the weekday: ")
print("The entered weekday is: ", weekday)

if weekday == "Monday":
    backup()
else:
    print("You have entered something different than Monday which is: ", weekday)