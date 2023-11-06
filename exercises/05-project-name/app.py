import requests

# your code here

url = "https://assets.breatheco.de/apis/fake/sample/project1.php"

response = requests.get(url)

data = response.json()

keys = []
values = []

for k, v in data.items():
    keys.append(k)
    values.append(v)


print(values[0])