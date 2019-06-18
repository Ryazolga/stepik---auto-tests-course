from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text

# Открыть страницу http://suninjuly.github.io/wait1.html
# Нажать на кнопку "Проверка"
# Проверить, что появилась надпись "Проверка прошла успешно"

#Тест падает из-за JS, который делает задержку на появление кнопки в 1 сек
#Исправленная версия в ниже в комментариях

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5) #вместо line 26
browser.get("http://suninjuly.github.io/wait1.html")

#time.sleep(1)


button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text