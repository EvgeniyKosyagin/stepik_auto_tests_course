from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    #нажимаем кнопку
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element_by_css_selector("button#book")
    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #ждем окрытия страницы
    time.sleep(1)
    #считываем переменную и передаем в функцию
    x_element = browser.find_element_by_id("input_value")
    x =x_element.text
    y = calc(x)
    #передаем результат в поле
    inputy=browser.find_element_by_id("answer")
    inputy.send_keys(y)
    #жмем принять результат
    button = browser.find_element_by_css_selector("button#solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
