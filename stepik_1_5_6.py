from selenium import webdriver

rootUrl = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(rootUrl)
elements = browser.find_elements_by_tag_name("input")
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()