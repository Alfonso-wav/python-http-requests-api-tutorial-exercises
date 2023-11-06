import requests

def get_titles():
    # Inicializa un arreglo vacío para almacenar los títulos
    titles = []
    posts = []
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    data = response.json()

    for i in data["posts"]:
        posts.append(i)
    
    for j in posts:
        if "title" in j:
            titles.append(j["title"])


    return titles




print(get_titles())

