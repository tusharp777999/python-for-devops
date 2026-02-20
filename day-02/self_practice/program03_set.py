days = {} #It will create empty dictionary not set.
print(type(days))

days = {"Sunday"}#If we don't want to use set() method and want to create the set we need to add any type of single value which is not in key:value pair it creates the set automatically.
print(type(days))

days = set()#Creates the empty set which contains only unique values duplicates are not present in it.
print(type(days))

days = {"Saturday", "Sunday", "Saturday", "Sunday"}
print(type(days))#Prints type of days which is set.
print(days)#Prints unique values only.

nums = [1, 2, 1, 1, 2, 3, 3, 3, 2, 1, 1, 6, 7, 7, 6, 5, 4, 3, 3, -1, -1, -5]#Its a list.
print(nums)#Prints list.

#You have scenario where you want unique values from the nums list we can achive this using following things.
nums = set(nums)#Converts list into set now the nums is set but we want it in list only so you can again convert it into list.
print(type(nums))
nums = list(nums)
print(type(nums))
print(nums)

#Other way to do it.
nums = [1, 2, 1, 1, 2, 3, 3, 3, 2, 1, 1, 6, 7, 7, 6, 5, 4, 3, 3, -1, -1, -5]#Its a list.
print(nums)
nums = list(set(nums))
print(nums)