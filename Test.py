import requests
import json

uid = "admin"
pw = "pw"
url = "http://127.0.0.1:8000"

accounts = [["admin", "pw"], ['testuser', 'test'], ['seokhyun', "password"]]
tokens = ["cfb819a052a919f57af87de37a463563688ebc3c", "b4fa73e1ab6ad9ba940310e3a1d2d1200fb6ff46", "af701771189f8d75b62ba343915fe96467c2d2cf"]
headers = {"Authorization": tokens[0]}

# Register
# res = requests.post(f"{url}/register/", json={'uid': accounts[2][0], "pw": accounts[2][1]})
# GetUser
# res = requests.get(f"{url}/user/info/2")
# Login
# res = requests.post(f"{url}/login/", json={'uid': uid, "pw": pw})
# Logout
# res = requests.get(f"{url}/logout", headers=headers)
# GetUsers
# res = requests.get(f"{url}/adm/user?page=0", headers=headers)
# ChangePw
# res = requests.post(f"{url}/user/changepw/", headers=headers, json={"newpw": "pw"})


# Add
# res = requests.post(f"{url}/word/add/", headers=headers, json={"word": "word", "kor": "kor", "eng": "eng"})
# Modify
# res = requests.post(f"{url}/word/modify/", headers=headers, json={"word": "word", "kor": "한글", "eng": "영어"})
# Delete
# res = requests.delete(f"{url}/word/delete/1", headers=headers)
# GetWord
# res = requests.get(f"{url}/word/info/1", headers=headers)
# GetWords
# res = requests.get(f"{url}/word/0", headers=headers)


# Add
# res = requests.post(f"{url}/study/add/", headers=headers, json={"wid": 1})
# Delete
# res = requests.delete(f"{url}/study/delete/1", headers=headers)
# GetStudies
res = requests.get(f"{url}/study/0", headers=headers)

# Add
# res = requests.post(f"{url}/notice/add/", headers=headers, json={"title": "title", "content": "content"})
# Modify
# res = requests.post(f"{url}/notice/modify/1", headers=headers, json={"title": "title", "content": "content1"})
# Delete
# res = requests.delete(f"{url}/notice/delete/1", headers=headers)
# GetNotices
# res = requests.get(f"{url}/notice/0", headers=headers)

print(res.json())
