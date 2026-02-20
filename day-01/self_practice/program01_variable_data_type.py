print("Hello World!!!")

#Variable: A variable in program means its a name within which we assign some values and that values can changes for that particular name is called variable.
#So, here "a" is a variable and its intial value is 100 then later we changed it to 200.
a = 100
a = 200
print(a) #Prints 200

#Constant: A value which does not changes is called it as constant. Like "yes" is the value it is constant or "no" it is also a constant which is not changes.
#"yes" is a value which is constant and "no" is also a value which is constant for the above example the 100 is a value which is also a constant same for 200. All values are constants.
a = "yes"
a = "no"
print(a)#Prints no

#Note: "=" is a assignment operator which assigns the value present in the left side to the right side variable.

'''
Operators: Which operates on variable to perform certain activity like addition,substraction etc Ex. +, -, *, /, % etc.
x + y: Here "+" is Operator and on which variable this operation is happeining it is called as Operands (x, y)
x + y = : It is called as Operation.
'''
x = 2
y = 3
print(x+y)#Prints 5

#Do any operation of your choice:
c = 100
d = 500
e = c * d
print("The multiplication of c & d: ", e)

'''
Data Type: It means what type of data you have and based on that you can perform operations and utilize the particular data as per your need.
int: It means a numeric value without decimal point which can be either negative or postive.
float: It means a numeric value with decimal point which can be either negative or positive.
str: It means string which is group of characters or digits enclosed in double quotes.
bool: It means boolean which is have only 2 fixed values to take the decision it can be True or False.
Note: type() function is used to get the type of the data of a particular variable.
'''

a = 10
print(a)
print(type(a))

b = 10.5
print(b)
print(type(b))

c = "Tushar"
print(c)
print(type(c))

d = True
print(d)
print(type(d))

'''
Interactive Shell: To open it just open your terminal and type "python3.14" whichever python version you have just type and press enter.
Ex: 
>python3.14 #It starts the Interactive Shell.

In this you can do REPL which means
R: Read
E: Evaluate
P: Print
L: Loop

>exit() #It exits from Interactive Shell.
'''
#Note: Always use snake case in python.