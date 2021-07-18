import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def count(x):
    return math.log(abs(12 * math.sin(x)), math.e)


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Edge(executable_path="../edgedriver_win32/msedgedriver.exe")
    browser.get(link)
    valuex = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(count(float(valuex))))
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
