from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://passport.yandex.ru/auth/welcome?origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru')
# assert "GeekBrains" in driver.title

elem = driver.find_element_by_id('passp-field-login')
elem.send_keys('contestbook@ya.ru')
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_id('passp-field-passwd')
elem.send_keys('link1789')
elem.send_keys(Keys.RETURN)

mesage_links = driver.find_elements_by_class_name('mail-MessageSnippet')
print(mesage_links)
links= []
for link in mesage_links:
    links.append(link.get_attribute('href'))

for i in links:
    print(i)
