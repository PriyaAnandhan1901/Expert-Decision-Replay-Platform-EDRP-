import requests

login = requests.post(
    "http://localhost:8000/api/auth/login",
    data={"username": "admin@test.com", "password": "secret123"}
)
token = login.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# Upload v1
f = open(r"C:\Users\GOPI\AppData\Local\Temp\test_upload.txt", "rb")
files = {"file": ("version_test_v1.txt", f, "text/plain")}
data = {"decision_id": "1"}
r1 = requests.post("http://localhost:8000/api/documents/upload", files=files, data=data, headers=headers)
f.close()
print("UPLOAD V1:")
print(r1.status_code, r1.json())
doc_id = r1.json()["id"]

# Upload v2 on top of it
f2 = open(r"C:\Users\GOPI\AppData\Local\Temp\test_upload.txt", "rb")
files2 = {"file": ("version_test_v2.txt", f2, "text/plain")}
r2 = requests.post(f"http://localhost:8000/api/documents/{doc_id}/new-version", files=files2, headers=headers)
f2.close()
print("UPLOAD V2:")
print(r2.status_code, r2.json())

# List by decision - should show only latest version
r3 = requests.get("http://localhost:8000/api/documents/by-decision/1", headers=headers)
print("LIST BY DECISION:")
print(r3.status_code)
for d in r3.json():
    print(d)

# History - should show both v1 and v2
r4 = requests.get(f"http://localhost:8000/api/documents/{doc_id}/history", headers=headers)
print("HISTORY:")
print(r4.status_code)
for d in r4.json():
    print(d)
