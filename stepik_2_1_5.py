from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

myUrl = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(myUrl)

equation = browser.find_element_by_css_selector("label > span:nth-child(2)")
x = equation.text
y = calc(x)
inputEq = browser.find_element_by_css_selector("#answer")
inputEq.send_keys(y)
chkbx = browser.find_element_by_css_selector("[for='robotCheckbox']")
chkbx.click()
rdbtn = browser.find_element_by_css_selector("[for='robotsRule']") #можно было поиск по id  со значением robotsRule
rdbtn.click()
button = browser.find_element_by_css_selector(".btn.btn-default")
button.click()

# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "Подтверждаю, что являюсь роботом".
# Выбрать radiobutton "Роботы рулят!".
# Нажать на кнопку Отправить.