import requests

response = requests.get(
    "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow",
    timeout=10,
).json()["items"]

for data in response:
    if data["answer_count"] == 0:
        print(data["title"])
        print(data["link"])
    else:
        print("skipped - data was empty")
    print("")
