import requests
responses = requests.get("https://www.google.com")
print(responses.text)