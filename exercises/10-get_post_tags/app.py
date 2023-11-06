import requests

def get_post_tags(post_id):
    # your code here
    # Inicializa un arreglo vacío para almacenar los títulos
    posts = []

    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    data = response.json()

    for i in data["posts"]:
        posts.append(i)

    for i in posts:
        if i["id"] == post_id:
            return i["tags"]


print(get_post_tags(146))