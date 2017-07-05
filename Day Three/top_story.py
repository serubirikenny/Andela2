import requests
from bs4 import BeautifulSoup


url = "http://www.monitor.co.ug/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

a = soup.find_all(class_="top-teaser")
for p in a:
    y = (p.text).strip()
    print(y)
