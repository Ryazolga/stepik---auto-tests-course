from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

span1 = browser.find_element_by_id("input_value")
x = span1.text
y = calc(x)
inputEq = browser.find_element_by_css_selector("#answer")
inputEq.send_keys(y)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
chkbx = browser.find_element_by_id("robotCheckbox")
chkbx.click()
rdbtn = browser.find_element_by_id("robotsRule")
rdbtn.click()

button.click()


# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "Подтверждаю, что являюсь роботом".
# Переключить radiobutton "Роботы рулят!".
# Нажать на кнопку "Отправить".