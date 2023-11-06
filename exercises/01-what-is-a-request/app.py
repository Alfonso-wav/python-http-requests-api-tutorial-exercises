import requests

url = "https://assets.breatheco.de/apis/fake/sample/hello.php"
response = requests.get(url)

print(response.status_code)