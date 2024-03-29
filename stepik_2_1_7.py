from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

myUrl = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(myUrl)

img = browser.find_element_by_tag_name("img")
x = img.get_attribute("valuex")
y = calc(x)
inputEq = browser.find_element_by_css_selector("#answer")
inputEq.send_keys(y)
chkbx = browser.find_element_by_id("robotCheckbox")
chkbx.click()
rdbtn = browser.find_element_by_id("robotsRule")
rdbtn.click()
button = browser.find_element_by_css_selector(".btn.btn-default")
button.click()

# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "Подтверждаю, что являюсь роботом".
# Выбрать radiobutton "Роботы рулят!".
# Нажать на кнопку "Отправить".