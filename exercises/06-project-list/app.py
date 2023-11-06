import requests

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"

response = requests.get(url)

data = response.json()

data2 = data[1]

print(data2["name"])