from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def count(x):
    return math.log(abs(12 * math.sin(x)), math.e)


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Edge(executable_path="../edgedriver_win32/msedgedriver.exe")
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()
    browser.switch_to.alert.accept()
    x = float(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(count(x)))
    browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
