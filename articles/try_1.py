import requests
from bs4 import BeautifulSoup









# Installs for BS
# pip install beautifulsoup4
# pip install lxml
# pip install html5lib


# req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
req = requests.get('https://news.ycombinator.com/news?p=1')
html = req.text #тут разметка
soup = BeautifulSoup(html, "lxml")
# print(soup)
# print(soup.prettify()) #pretty print

# for link in soup.find_all('a'):
#     print(link.get('href'))

posts = soup.find_all("a", class_="storylink")
# print(links)

posts = posts[:1]
for item in posts:
    title = str(item.get_text())
    url = item['href']
    #Saving posts to DB
    # new_post = Article(title=title, url=url)
    # new_post.save()


    # print(f"{title} \n {url}")
    # print(str(item.get_text()))
    # print(link, "\n")