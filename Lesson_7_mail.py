from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://mail.ru/')
# assert "GeekBrains" in driver.title

elem = driver.find_element_by_id('mailbox:login')
elem.send_keys('contestbook@mail.ru')
elem.send_keys(Keys.RETURN)
assert "Mail.ru: почта, поиск в интернете, новости, игры" in driver.title
elem = driver.find_element_by_id('mailbox:password')
elem.send_keys('link1789')
elem.send_keys(Keys.RETURN)

""" В данно месте начинаются проблемы - вроде на странице очевидно где каждое входящее письмо, соответственно их нужно просто 
все собрать в 1 список и потом у каждого вытащить ссылку, но список пустой формируется. При этом я проовал сначала в список
запихнуть верхний див, а в нем уже перебрать все письма и из них вытащить ссылку - но все равно пустой возвращает, Вы могли 
бы подсказать в чем дело"""
mesage_links = driver.find_elements_by_class_name('js-letter-list-item')
print(mesage_links)
links= []
for link in mesage_links:
    links.append(link.get_attribute('href'))


for i in links:
    print(i)
