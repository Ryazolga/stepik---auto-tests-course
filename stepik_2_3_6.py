from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
url = "http://suninjuly.github.io/redirect_accept.html"
browser.get(url)

button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

inputX = browser.find_element_by_id("input_value")
x = inputX.text
y = calc(x)
inputEnter = browser.find_element_by_id("answer")
inputEnter.send_keys(y)
button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()

# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ