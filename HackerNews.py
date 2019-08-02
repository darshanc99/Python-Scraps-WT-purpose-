#Import Dependencies
import requests
import ast

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
payload = "{}"
response = requests.request("GET", url, data=payload)
a = response.text
#print(type(a))

#Converting string list into list
a = ast.literal_eval(a)

for i in range(len(a)):
	url = "https://hacker-news.firebaseio.com/v0/item/"+str(a[i])+ ".json"
	payload = "{}"
	response = requests.request("GET", url, data=payload)
	dict_response = response.json()
	#print(dict_response)
	print("Title: " + str(dict_response['title']))
	print("Type:",str(dict_response['type']))
	if 'url' in dict_response.keys():
		print("URL: " + (dict_response['url']),"\n")
