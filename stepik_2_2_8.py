from selenium import webdriver
import os

browser = webdriver.Chrome()
url = "http://suninjuly.github.io/file_input.html"
browser.get(url)

inputName = browser.find_element_by_name("firstname")
inputName.send_keys("Olya")
inputLastName = browser.find_element_by_name("lastname")
inputLastName.send_keys("RyazOlya")
inputEmail = browser.find_element_by_name("email")
inputEmail.send_keys("RyazOlya@dom.ru")

file = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'empty.txt')
file.send_keys(file_path)

button = browser.find_element_by_css_selector(".btn.btn-primary")
button.click()

#alert = browser.switch_to.alert
#alert.accept()


# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Отправить"