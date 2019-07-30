import requests
username = input("Enter the github username:")
request = requests.get('https://api.github.com/users/'+username+'/repos?per_page=1000')
json = request.json()
for i in range(0,len(json)):
	print("Project Number:",i+1)
	print("Project Name:",json[i]['name'])
	print("Project URL:",json[i]['svn_url'],"\n")
