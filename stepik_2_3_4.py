from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
url = "http://suninjuly.github.io/alert_accept.html"
browser.get(url)

button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

inputX = browser.find_element_by_id("input_value")
x = inputX.text
y = calc(x)
inputEnter = browser.find_element_by_id("answer")
inputEnter.send_keys(y)
button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()

# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом