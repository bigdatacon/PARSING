from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://e.mail.ru/login')
# assert "GeekBrains" in driver.title
assert "Вход - Почта Mail.ru" in driver.title

""""Не смог залогиниться, потому что кнопка для ввода почты имеет код, тот что ниже, но ни один варинант поиска не находит
окно ввода, ниже приведены те варианты которые пробовал
окно ввода, ниже приведены те варианты которые пробовал
<input name="Login" placeholder="Имя аккаунта" autocapitalize="off" autocomplete="username" autocorrect="off" type="text" class="c0155" value="">"""

#Пробовал:
# elem = driver.find_element_by_css_selector('input.c0155')
# elem = driver.find_element_by_name("Login")

# elem = driver.find_element_by_class_name('c0155')
# elen = driver.find_element_by_tag_name(name, "Login")
# elem = driver.find_element_by_xpath('//input[@class ="c0155"]')


elem.send_keys('contestbook@mail.ru')
elem.send_keys(Keys.RETURN)
assert "Вход - Почта Mail.ru" in driver.title

