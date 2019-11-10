from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get('https://www.mvideo.ru/televizory-i-video')
time.sleep(5)
print('Вход на страницу МВИДЕО')

while True:
    try:
        iframe = driver.find_element_by_class_name('flocktory-widget')
        driver.switch_to.frame(iframe)
        button = WebDriverWait(driver,15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'PushTip-close'))
        )
        button.click()
        """ После того как перешел на всплывающий фрейм нужно вернуться обратно, пробовал варианты те что ниже
        но работает почему то только повторный вход на страницу
        - driver.get('https://www.mvideo.ru/televizory-i-video'), Вы знаете еще другой вариан как можно решить данную 
        проблему не открывая страницу повторно?"""
        # driver.switch_to_default_content()
        # driver.back()
        driver.get('https://www.mvideo.ru/televizory-i-video')
        """тут как правило появлется еще 1 всплывающее окно, его тоже закрываем"""
        """Вот здесь самый сложный нюанс который я не понял: всплывающее окно появляется с задержкой, 
        соответственно если не нажимать слип, то данные начинают собираться, но почему то собираются только ссылки
        хотя описание ровно в том же классе что и ссылка но не собирается, и не собирается цена(там разные варианты 
        классов пробовал. Но если сделать все как надо и сделать слип чтобы окно закрылось и только потом листать страницы
        то в итоге вообще ничего не собирает, дажы ссылки, но при этом я смотрел код - ничего не поменялось и 
        ссылки и описание ровно в тех же тегах -Вы могли бы сказать почему так? """
        # time.sleep(7)
        while True:
            try:
                iframe = driver.find_element_by_class_name('flocktory-widget')
                driver.switch_to.frame(iframe)
                button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'Widget-close'))
                )
                #path-1
                button.click()

                driver.get('https://www.mvideo.ru/televizory-i-video')
            except Exception as e:
                print('Не было всплывающего окна 2')
                break
    except Exception as e:
        print('Не было всплывающего окна')
        break

pages = 1
while pages<6:
    try:
        button = WebDriverWait(driver,30).until(
            # EC.presence_of_element_located((By.CLASS_NAME, 'catalog__pagination-button'))
            EC.element_to_be_clickable((By.CLASS_NAME, 'sel-hits-button-next'))
        )
        # button = driver.find_element_by_class_name('catalog__pagination-button')
        button.click()
        pages +=1
        print(f'переход на страницу {pages} произведен')
    except Exception as e:
        print(e)
        break

goods = driver.find_elements_by_class_name('product-tile-info')

goods_list = []
good_dict = {}
for good in goods:
    good_dict['descr'] = good.find_element_by_class_name('sel-product-tile-title').text
    good_dict['link'] = good.find_element_by_class_name('sel-product-tile-title').get_attribute('href')
    # good_dict['price'] = good.find_element_by_class_name('sel-product-tile-price').text
    good_dict['price'] = good.find_element_by_class_name('product-price').text
    goods_list.append(good_dict)

for i in goods_list:
    print(i)
