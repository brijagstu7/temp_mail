import requests
import hashlib
import sys

name = sys.argv[1]
domain = "@mailkept.com"
s2b = bytes(name+domain, 'utf-8')
m = hashlib.md5()

m.update(s2b)

url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/"+m.hexdigest()+'/'

headers = {
    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com",
    'x-rapidapi-key': "e866adcfedmshf7a624373d25249p1f1090jsn9c676a2190dc"
    }

response = requests.request("GET", url, headers=headers)
try:
    json_strs = eval(response.text)  # error may occur due to network conditions
except BaseException:
    print("Problem with server or network")
    exit(1)
try:
    json_data = json_strs[-1]
except BaseException:
    print("no e-mail")
    exit(1)
# json_data = json.loads(json_str)  # no need to parse, since already evaluated
mail_content = json_data["mail_subject"]
print(mail_content)
