from bs4 import BeautifulSoup
import requests
import time

texts = requests.get("http://data.tainan.gov.tw/dataset/t-bike")

text = BeautifulSoup(texts.text, "html.parser")

text = text.find_all("ul", class_="dropdown-menu")[2].find_all("a")[1]


print(text.get("href"))
texts = requests.get(text.get("href"))
texts = texts.json()

file_str = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
print(file_str)
f = open("./bike_data/"+file_str, "w+")

keys = []
for x in texts[0]:
    keys.append(x)

row = ""
for x in texts:
    for key in keys:
        row += str(x[key]) + ","
    f.write(row+"\n")
    row = ""

f.close()
print(len(texts))
