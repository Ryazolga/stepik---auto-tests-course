from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000")
    )
button = browser.find_element_by_id("book")
button.click()

inputX = browser.find_element_by_id("input_value")
x = inputX.text
y = calc(x)
inputEnter = browser.find_element_by_id("answer")
inputEnter.send_keys(y)
buttonSolve = browser.find_element_by_id("solve")
buttonSolve.click()