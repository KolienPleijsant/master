# """
# To see an example of the Wikipedia API JSON look at this url:
# https://en.wikipedia.org/api/rest_v1/page/summary/Japanese_cuisine
# """
import requests

def api_call(title, value):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    req = requests.get(url)
    data = req.json()
    if req.status_code != 200:
        print(f"We got an error: {req.status_code}")
        exit()
    return data[f"{value}"]

title = input("Give an article: ").strip()
value = input("Description or extract? ").strip().lower()
data = api_call(title, value)

print(f"Here is {value} for {title}:")
print(data)