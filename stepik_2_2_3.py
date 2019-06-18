from selenium import webdriver
from selenium.webdriver.support.ui import Select

myUrl = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(myUrl)

span1 = browser.find_element_by_id("num1")
x1 = span1.text
span2 = browser.find_element_by_id("num2")
x2 = span2.text
y = int(x1) + int(x2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(str(y))
button = browser.find_element_by_css_selector(".btn.btn-default")
button.click()

# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Отправить"