from selenium import webdriver
import time
from selenium.webdriver.common.by import By



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Edge(executable_path="../edgedriver_win32/msedgedriver.exe")
    browser.get(link)
    a = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    b = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    browser.find_element(By.CSS_SELECTOR, "#dropdown").click()
    browser.find_element(By.CSS_SELECTOR, '[value="{}"]'.format(str(a+b))).click()
    browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
