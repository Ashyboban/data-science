import requests
from bs4 import BeautifulSoup

print("23mca030 : GEORGE SCARIA")


def getdata(url):
    r = requests.get(url)
    return r.content

htmldata = getdata("https://sjcetpalai.ac.in/")
soup = BeautifulSoup(htmldata, 'html.parser')
pr = len(soup.find_all('p'))
print("<P> tag count:", pr)
for data in soup.find_all('p'):
    print(data.get_text())
