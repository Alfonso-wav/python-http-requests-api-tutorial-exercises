import requests

# your code here

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"

response = requests.get(url)

data = response.json()

first_d = data["posts"][0]["title"]

print(first_d)