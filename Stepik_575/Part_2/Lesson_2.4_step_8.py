# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


'''
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    Нажать на кнопку "Book"
    Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100,
используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
'''

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")



#
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #
    while True:
        if browser.find_element_by_id('price').text == '$100':
            print(browser.find_element_by_id('price').text)
            button = browser.find_element_by_id('book')
            button.click()
            break

    #
    browser.execute_script("window.scrollBy(0, 200);")

    # ТАщим "х" и тыкаем его в уравнение
    calc_x = browser.find_element_by_id('input_value')
    answer = calc(calc_x.text)

    # вставляю текст в форму
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(answer)

    #Тыкам на кнопку
    button = browser.find_element_by_id('solve')
    button.click()

finally:
    #
    confirm = browser.switch_to.alert
    print(confirm.text.split(': ')[-1])

    # закрываем браузер после всех манипуляций
    browser.quit()
