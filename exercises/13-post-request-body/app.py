import requests

myobj = {
    "id":2323,
    "title": "Very big project"
}

resp = requests.post("https://assets.breatheco.de/apis/fake/sample/save-project-json.php", json = myobj)


print(resp.text)