import requests

# your code here

url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"

response = requests.get(url)

data = response.json()

last_data = data[-1]

last_image = last_data["images"][-1]

print(last_image)
