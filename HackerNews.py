#Import Dependencies
import requests
import ast

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
payload = "{}"
response = requests.request("GET", url, data=payload)
a = response.text
print(type(a))

#Converting string list into list
a = ast.literal_eval(a)

for i in range(len(a)):
	url = "https://hacker-news.firebaseio.com/v0/item/"+str(a[i])+ ".json"
	payload = "{}"
	response = requests.request("GET", url, data=payload)
	print(response.text)