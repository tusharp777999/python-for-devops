#Get input from user and print it.
environment = input()#It takes input from the user which will be in string form and to show the message to the user we need to use the below format of this input method.
print(environment)
print(type(environment))#It gives output as a string.

environment = input("Enter the Environment: ")#It takes input from user which will be in string form and the input is a mehtod which also takes the parameter which shows the message to the user
print(environment)
print(type(environment))

#Take two inputs and do the arithmatic operations on it.
a = int(input("Enter the first number: "))#Here we need to do type-casting as we know input() method gives us string type data.
b = int(input("Enter the second number: "))#Here we need to do type-casting as we know input() method gives us string type data.

print(type(a))#It gives output as a integer.
print(type(b))

print("Addition is: ", a + b)
print("Substraction is: ", a - b)
print("Multiplication: ", a * b)

environment = input("Enter the Environment: ")
print("The user input is: ", environment)

#if-else is a Conditional Statement which works on boolean condition, Here we are using conditonal operators like ==, !=, <=, >= etc.
if environment == "PROD":
    print("Don't deploy on Friday.")
elif environment == "UAT":
    print("Take backup and test well.")
else:
    print("Safe to deploy on any day.")