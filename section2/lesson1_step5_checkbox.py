from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def count(x):
    return math.log(abs(12 * math.sin(x)), math.e)


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Edge(executable_path="../edgedriver_win32/msedgedriver.exe")
    browser.get(link)
    num = count(float(browser.find_element(By.CSS_SELECTOR, "#input_value").text))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(num))
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
