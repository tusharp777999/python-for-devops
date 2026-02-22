import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url=url)#We are hitting the GET request.
print(response)#Printing the HTTP status code.

data = response.json()

print(data)#To print the json data present in response.
print(type(data))#It type is dictionary.

#How to iterate data of above response.
for key, value in data.items():
    print(key, ":", value)

#How to apply logics.
for key, value in data.items():
    if key == "completed":
        if value == False:
            print("Data is not complete.")

for key, value in data.items():
    if key == "userId":
        if value in [2, 1, 5, 4]:
            print("User found.")


