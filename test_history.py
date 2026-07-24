import requests

login = requests.post(
    "http://localhost:8000/api/auth/login",
    data={"username": "admin@test.com", "password": "secret123"}
)
token = login.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Edit decision 1 - change the title
r1 = requests.put(
    "http://localhost:8000/api/decisions/1",
    json={"title": "Choose cloud provider (v2 test)"},
    headers=headers,
)
print("UPDATE:")
print(r1.status_code, r1.json())

# Fetch history
r2 = requests.get("http://localhost:8000/api/decisions/1/history", headers=headers)
print("HISTORY:")
print(r2.status_code)
for entry in r2.json():
    print(entry)
