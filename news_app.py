import requests
import json
query = input("What type of news are you interested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-09&sortBy=publishedAt&apiKey=d57e96f9dddb4577b3413e4ddfdefc86"
response = requests.get(url)
news = json.loads(response.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["url"])
    print("<---------------------------------------------------------------------------------------->")