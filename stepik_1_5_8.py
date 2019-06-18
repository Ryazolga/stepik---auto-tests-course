from selenium import webdriver

rootUrl = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(rootUrl)

input1 = browser.find_element_by_css_selector(".first_block .first")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector(".first_block .second")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector(".first_block .third")
input3.send_keys("Smolensk@mail.ru")
button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()