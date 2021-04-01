import urllib.request
import bs4

# html情報を取得
html = urllib.request.urlopen('https://news.yahoo.co.jp/topics/top-picks')
# print(html)

soup = bs4.BeautifulSoup(html,'html.parser')
# print(soup)

h1_elem = soup.find_all('div', class_='newsFeed_item_title')
# print(h1_elem)

for news in h1_elem:
    print(news.text)
