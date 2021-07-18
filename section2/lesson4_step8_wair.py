from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def count(x):
    return math.log(abs(12 * math.sin(x)), math.e)


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Edge(executable_path="../edgedriver_win32/msedgedriver.exe")
    browser.get(link)
    WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )
    browser.find_element(By.CSS_SELECTOR, "#book").click()
    x = float(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(str(count(x)))
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()