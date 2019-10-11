def Ancestors (a,k,url):
    try:
        if a[1:7]=="sports":
            k.append(url+a)
    except TypeError:
        print("Not your fault")
    return k
import json
import requests
from bs4 import BeautifulSoup as s
url="https://www.bhaskar.com/sports/72"
data=requests.get(url)

file='''
{   
    "urls":[]
}
'''

soup=s(data.text,'html.parser')
b=[]
for i in soup.find_all('a'):
    b=Ancestors(i.get('href'),b,url)
text=json.loads(file)

for i in b:
    text['urls'].append(i)



with open("all_sportsnews_urls.json",'w') as f:
    json.dump(text,f)