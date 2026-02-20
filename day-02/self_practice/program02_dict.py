info = {}#Creates the empty dictionary.
print(info)#Prints empty dictionary.
print(type(info))

info = dict()#Another way to create empty dictionary.
print(type(info))

info = {
    "name":"Tushar",
    "city":"Pune",
    "qualification":"BE",
    "age":35,
    "salary":17,
    "married":True,
    "favorites":["Teaching", "Learning", "Watching Movies"]
}#Way to declare the dictionary which contains key and value pair.

print("I live in ", info["city"])#To print the value from the dictionary we need to use key to fetch its relevant value.
#print("I love ", info["favorite"])#Its possible while fetching the data using key the key spelling can be wrong and it will give you error to avoid such issue we need to use get() method.
print("I love ", info.get("favorite"))#It handles wrong key as we can see there is no favorite key it is favorites but it will not gives error it simply returns None.
print("I love ", info.get("favorite", "Not found."))#If you want your custom error instead of None you can provide as a argument to the method as shown.

info.update({"channel":"Tushar's Devops"})#To add into previous created dictionary.
print(info)

for key in info:#If we iterate normally it gives only keys not the values.
    print(key)

for key in info.keys():#Another way to get the keys only.
    print(key)

for value in info.values():#To get only values we need to use values() method.
    print(value)

for key, value in info.items():#Items() method gives you the entire entry like key and value as well based on this we can fetch both the things at a time.
    print(key," : ", value)

for key in info:#Another way to get the key and its value.
    print(key, " : ", info.get(key))