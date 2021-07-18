from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Edge(executable_path="../edgedriver_win32/msedgedriver.exe")
    browser.get(link)
    browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))).click()
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div:nth-child(1) > input").send_keys("Dima")
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div:nth-child(2) > input").send_keys("Tigran")
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div:nth-child(3) > input").send_keys("Moscow")
    browser.find_element(By.CSS_SELECTOR, "#country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
