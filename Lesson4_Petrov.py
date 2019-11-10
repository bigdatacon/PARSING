import requests
from pprint import pprint
import json
from bs4 import BeautifulSoup as bs
import re
from lxml import html
headers = {'accept': '*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}


"""Ниже приведены ссылки которые я забивал к chropath и все подсвечивалось, но когда делаю гет запрос, приходят пустые данные,
в итоге не работает ничего (хотя в хропасе можете проверить ссылки верные, но написал как бы я реализовал перенос данных если
бы ссылки работали"""
# С мейла
#
# Главная и остальные новости с мейла
# //div[@class = 'news-item__content']/h3|//div[@class='news-item__inner']/a[last()]
#
# дата публикации (для этого нужно перейти на страницу новости)
# //span[@data-ago_content]
#
# источник (для этого нужно перейти на страницу новости)
#
# //span[@class='breadcrumbs__item']//span[@class = 'link__text']
#
# Ссылки
##все
# //div[@class = 'news-item__content']/h3/@href|//div[@class='news-item__inner']/a[last()]/@href
## все кроме главной
# //div[@class='news-item__inner']/a[last()]/@href

main_link='https://news.mail.ru/'
req = requests.get(main_link, headers=headers)
root = html.fromstring(req.text)
DATA = {}
dates = []
sources = []

hrefs = root.xpath('//div[@class = "news-item__content"]/h3/@href|//div[@class="news-item__inner"]/a[last()]/@href')
news = root.xpath('//div[@class = "news-item__content"]/h3/text()')
### переходим по ссылке чтобы взть со страницы с новостью дату и источник
for i in hrefs:

    href_link = i
    req_deep = requests.get(href_link, headers=headers)
    root_deep = html.fromstring(req_deep.text)
    source = root.xpath('//span[@class="breadcrumbs__item"]//span[@class = "link__text"]')
    date = root.xpath('//span[@data-ago_content]')
    dates.append(date)
    sources.append(source)
for j in range(len(news)):
    for i in news:
        for n in hrefs:
            for m in dates:
                for x in sources:
                    DATA[j] = ((i,n,m,x))
print(DATA)

