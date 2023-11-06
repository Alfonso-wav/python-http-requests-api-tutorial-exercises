import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
data = response.json()
keys = []
values = []

for key, value in data.items():
    keys.append(key)
    values.append(value)

output = f"Current time: {values[0]} hrs {values[1]} min and {values[2]} sec"
print(output)