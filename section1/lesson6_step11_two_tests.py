from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Edge(executable_path='D:\\Python\\SeleniumTest\\edgedriver\\msedgedriver.exe')
    browser.get(link)

    # TODO: Автозаполнение формы регистрации
    first_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
    first_name.send_keys('Dima')

    last_name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
    last_name.send_keys('Borisovich')

    email = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    email.send_keys('otsilka@gmail.com')

    phone = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[1]/input')
    phone.send_keys('+78005553535')

    adress = browser.find_element_by_xpath('/html/body/div/form/div[2]/div[2]/input')
    adress.send_keys('Gde-to givu')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.close()
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла
