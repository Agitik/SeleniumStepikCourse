from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def count(x):
    return math.log(abs(12 * math.sin(x)), math.e)


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Edge(executable_path="../edgedriver_win32/msedgedriver.exe")
    browser.get(link)
    x = float(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(count(x)))
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
