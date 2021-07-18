from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Edge(executable_path="../edgedriver_win32/msedgedriver.exe")
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)").send_keys("Dima")
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)").send_keys("Tolochek")
    browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)").send_keys("tolochek.reg@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
