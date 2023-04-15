from bs4 import BeautifulSoup
import lxml

with open("index.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print(soup.title.string)
# print(soup.prettify())
all = soup.find_all(name="a")
for teg in all:
    # print(teg.getText())
    # print(teg.get("href"))
    pass
# print(all)

heading = soup.find(name="h1", id="heading")
# print(heading)

params = soup.find(name="p", class_="param")
# print(params.text)


urls = soup.select_one(selector="ul li a")
# print(urls)

# ________________________________
import requests as req

res = req.get(url="https://news.ycombinator.com/newest")
res.raise_for_status()
data = res.text

soup = BeautifulSoup(data, "lxml")
link = soup.select(selector=".titleline > a:first-child")
article_texts = []
article_links = []
for items in link:
    article_texts.append(items.getText())
    article_links.append(items.get("href"))
article_upvote = [
    (int(score.text.strip(" points")))
    for score in soup.find_all(name="span", class_="score")
]

output = max(article_upvote, key=lambda x: x)
output_index = article_upvote.index(output)
upvote_article_text = article_texts[output_index]
upvote_article_link = article_links[output_index]
print("output_index : ", output_index)
print("article_upvote : ", upvote_article_link)
print(upvote_article_text)
