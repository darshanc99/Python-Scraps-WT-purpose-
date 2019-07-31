#Import Dependencies
import requests
import ast

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
payload = "{}"
response = requests.request("GET", url, data=payload)
a = response.text


#Converting string list into list
a = ast.literal_eval(a)

for i in range(2):
	url = "https://hacker-news.firebaseio.com/v0/item/"+str(a[i])+ ".json"
	payload = "{}"
	response = requests.request("GET", url, data=payload)
	dict_response = response.json()
	print("Title: " + str(dict_response['title']))
	print("URL: " + str(dict_response['url']))
	#print(dict_response)
	
