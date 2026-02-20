#Ways to create a list:
a = []#First way to create empty list.
a.append(6)#Append the data to the list
print(type(a))#It prints <list>

a = list()
a.append(6)#Append the data to the list
print(type(a))#It prints <list>

#Here the issue is we have only one variable within we can able to add only one value if you try to add any new value it will overwrite it.
a = 100
a = 200
print(a)#It prints 200
print(type(a))#It prints <int>

#Here using single variable we can able to add multiple value of different types.
a = []
print(type(a))#It prints <list>

a = [100, 200, 300, True, 4.6]
print(a)#It prints all list values.
print(type(a))#It prints <list>

a.append(500)#To add data in the existing list.
print(a)#It prints list with updated list data.

clouds = list()#Second way to create a list.
print(type(clouds))
clouds.append("AWS")
clouds.append("Azure")
clouds.append("GCP")
clouds.append("Alibaba")
clouds.append("IBM")
clouds.append("Utho")
print(clouds)
print("The length of clouds list is: ", len(clouds))#To get the length of list we use len() function.
print("The cloud world leader: ", clouds[0])#To get the data from list from a particular index.
print("Indian cloud platform: ", clouds[5])
print("Cloud platform which is last in list: ", clouds[-1])#In list from left to right the indexing goes like 0 (positive series) and from right to left it starts from -1 (negative series).

print(dir(clouds))#Dir() is manual which tells what to do and what we can able to use with the list.
print(clouds.count.__doc__)#Here the clouds is a list and it has count method when we want to know what that mehtod does we have _doc_ attribute for it.

for cloud in clouds:#To print all the list one by one
    print(cloud)

for cloud in clouds:
    if cloud == "AWS":
        print("Market Leader.")
    elif cloud == "Azure" or cloud == "GCP":
        print("Covered in this course.")
    elif cloud == "Utho":
        print("Indian cloud.")
    else:
        print("Other things are not covered.")