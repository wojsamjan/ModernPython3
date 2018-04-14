import requests


url = "https://icanhazdadjoke.com/"
# response = requests.get(url, headers={"Accept": "text/html"})
# response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(url, headers={"Accept": "application/json"})

# print(response.text)
# print(type(response.text))  # str

data = response.json()
# print(type(data))  # dict
print(data["joke"])

print(f"status: {data['status']}")
print(f"status: {response.status_code}")
