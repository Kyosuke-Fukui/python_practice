from urllib.request import urlopen
from bs4 import BeautifulSoup

# 1.Get a html.
with urlopen('https://www.yoheim.net') as res:
    html=res.read().decode("utf-8")

# 2.Load ahtml by BeautifulSoup.
soup=BeautifulSoup(html,'html.parser')

# 3.Get items you want.
titles=soup.select(".articleListItem h2")
titles=[t.string for t in titles]

#Check results.
from pprint import pprint
pprint(titles[:4])


