# import requests

# # Request example
# target = "http://google.com"
# response = requests.get(url=target)
# print(response.text) 

import json
# JSON example
user = {
    "id": "gildong",
    "password": "192837",
    "age": 30,
    "hobby": ["football", "programming"]
}

json_data = json.dumps(user, indent = 4) # Encoding
data = json.loads(json_data) # Decoding
print(data)
print(json_data)

with open("user.json", "w", encoding = "utf-8") as file:
    json.dump(user, file, indent = 4)

