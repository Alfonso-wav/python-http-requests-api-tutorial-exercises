import requests

def get_attachment_by_id(attachment_id):
    # your code here
    posts = []

    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url)
    data = response.json()

    for i in data["posts"]:
        posts.append(i)

    print("IDs in data:", [i.get("id") for i in posts])

    for i in posts:
        if "id" in i and i["id"] == attachment_id:
            return i.get("title")
        
    return None 

print(get_attachment_by_id(135))